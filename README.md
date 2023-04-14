# Odoo-S3-Bukcet-Backup

# Odoo Sales Backup to AWS S3

This Python script allows you to automate the process of backing up your Odoo sales data, including product information and quantities, to a secure Amazon Web Services (AWS) S3 bucket. By using this script, you can ensure that your critical sales data is always backed up and stored offsite, improving your data security and business continuity.

## Features

- Fetches sales data from your Odoo instance
- Retrieves detailed product information and quantities for each sale order
- Saves the consolidated data as a JSON file
- Uploads the backup file to an AWS S3 bucket
- Removes the local copy of the backup file to conserve storage space and maintain data security
- Can be scheduled to run automatically at specific intervals for continuous and up-to-date backups

## Requirements

- Odoo 15
- Python 3.6+
- boto3 library (`pip install boto3`)
- Properly configured AWS credentials

## Setup

1. Clone or download this repository to your local machine.

2. Open the `odoo_sales_backup_to_s3.py` script in your favorite text editor.

3. Replace the placeholders for Odoo credentials and connection details:

4. Replace the placeholders for AWS credentials and S3 bucket configuration:

5. Save your changes and close the script.

## Usage

To run the script manually, open a terminal or command prompt, navigate to the directory containing the script, and run:

```bash
python odoo_sales_backup_to_s3.py

