import boto3
import json
import os
from datetime import datetime
from xmlrpc import client as xmlrpclib

# Odoo credentials and connection
url = 'http://your_odoo_url'
db = 'your_odoo_database'
username = 'your_odoo_username'
password = 'your_odoo_password'

# AWS credentials and configurations
aws_access_key_id = 'your_aws_access_key_id'
aws_secret_access_key = 'your_aws_secret_access_key'
s3_bucket_name = 'your_s3_bucket_name'

# Establishing the connection to Odoo
common = xmlrpclib.ServerProxy('{}/xmlrpc/2/common'.format(url))
uid = common.authenticate(db, username, password, {})

# Checking if the authentication was successful
if uid == 0:
    raise Exception("Authentication failed. Please check your Odoo credentials.")

# Connecting to the Odoo object API
models = xmlrpclib.ServerProxy('{}/xmlrpc/2/object'.format(url))

# Fetching sales and sales info
sales_data = models.execute_kw(db, uid, password,
    'sale.order', 'search_read',
    [[]],
    {'fields': ['name', 'partner_id', 'date_order', 'amount_total', 'order_line']})

# Fetching product info and quantity for each sale order
for sale in sales_data:
    order_lines = models.execute_kw(db, uid, password,
        'sale.order.line', 'read',
        [sale['order_line']],
        {'fields': ['product_id', 'name', 'product_uom_qty']})
    sale['order_line'] = order_lines

# Saving the sales data with product info and quantities to a JSON file
backup_filename = 'sales_backup_{}.json'.format(datetime.now().strftime('%Y%m%d_%H%M%S'))
with open(backup_filename, 'w') as backup_file:
    json.dump(sales_data, backup_file)

# Creating an S3 client
s3 = boto3.client('s3', aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key)

# Uploading the backup file to the S3 bucket
with open(backup_filename, 'rb') as backup_file:
    s3.upload_fileobj(backup_file, s3_bucket_name, backup_filename)

# Removing the backup file from the local system
os.remove(backup_filename)

print("Sales data with product info and quantities backup completed successfully.")
