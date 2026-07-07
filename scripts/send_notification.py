#!/usr/bin/env python3
"""
Send email notifications for workflow completion
"""

import os
import sys
import json
import logging
import smtplib
import argparse
from pathlib import Path
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('logs/send_notification.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

load_dotenv()

def send_notification(status='success'):
    """Send email notification"""
    logger.info(f"Sending {status} notification...")

    try:
        # Get email configuration from environment
        smtp_server = os.getenv('SMTP_SERVER', 'smtp.promega.com')
        smtp_port = int(os.getenv('SMTP_PORT', '587'))
        smtp_user = os.getenv('SMTP_USER', 'spark-forge@promega.com')
        smtp_password = os.getenv('SMTP_PASSWORD', '')
        recipients = os.getenv('NOTIFICATION_RECIPIENTS', '').split(',')

        if not smtp_password:
            logger.warning("SMTP_PASSWORD not configured, skipping notification")
            return

        # Create email message
        msg = MIMEMultipart('alternative')
        msg['Subject'] = f"Spark & Forge Biweekly Cycle {'Complete' if status == 'success' else 'FAILED'}"
        msg['From'] = smtp_user
        msg['To'] = ', '.join(recipients)

        # Create email body
        if status == 'success':
            body = """
Hi Team,

Your Spark & Forge biweekly automation cycle has completed successfully.

📊 Summary:
- New entries created and indexed
- Trend analysis complete
- RED/YELLOW/GREEN signals flagged
- Living Index updated

📁 Files:
- Living Index: Z:\\R&D\\R&D Meeting\\AI-Spark-Forge\\Spark_Forge_Index.xlsx
- Biweekly Report: Z:\\R&D\\R&D Meeting\\AI-Spark-Forge\\Biweekly_Reports\\

Next cycle: Tuesday, [date] at 9:00 AM PT

---
Spark & Forge Automation System
"""
        else:
            body = """
Hi Team,

⚠️ The Spark & Forge biweekly automation cycle FAILED.

Please check the logs and contact IT if needed.

---
Spark & Forge Automation System
"""

        msg.attach(MIMEText(body, 'plain'))

        # Send email
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(smtp_user, smtp_password)
            server.send_message(msg)

        logger.info(f"✅ Notification sent to {len(recipients)} recipients")

    except Exception as e:
        logger.error(f"Error sending notification: {e}")

def main():
    parser = argparse.ArgumentParser(description='Send Spark & Forge notifications')
    parser.add_argument('--status', default='success', choices=['success', 'failure', 'quarterly'])
    args = parser.parse_args()

    send_notification(args.status)

if __name__ == '__main__':
    main()
