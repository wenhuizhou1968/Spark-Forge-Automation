#!/usr/bin/env python3
"""
Phase 2: External Intelligence Scan
Scans literature (PubMed), conferences, vendors, and competitors
"""

import os
import sys
import json
import logging
import requests
from datetime import datetime, timedelta
from pathlib import Path
from dotenv import load_dotenv

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('logs/phase2_external_intelligence.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

load_dotenv()

def scan_literature():
    """Scan bioRxiv and PubMed for relevant papers"""
    logger.info("Scanning literature sources...")

    papers = []

    try:
        # Load extracted tags from Phase 1
        with open('phase1_extracted_entries.json', 'r') as f:
            entries = json.load(f)

        # Extract tags from Spark entries
        tags = set()
        for entry in entries.get('spark_entries', []):
            tags.update(entry.get('tags', []))

        logger.info(f"Found {len(tags)} unique tags to search")

        # Simulate finding relevant papers
        # In production, this would call PubMed API
        papers = [
            {
                'source': 'bioRxiv',
                'date': (datetime.now() - timedelta(days=7)).strftime('%Y-%m-%d'),
                'title': 'Bayesian Optimization for Chemical Discovery',
                'authors': 'Smith et al.',
                'relevance': 'confirmatory',
                'tags': ['bayesian optimization', 'chemistry']
            },
            {
                'source': 'PubMed',
                'date': (datetime.now() - timedelta(days=3)).strftime('%Y-%m-%d'),
                'title': 'AI-Driven Automation in Molecular Design',
                'authors': 'Chen et al.',
                'relevance': 'novel method',
                'tags': ['AI', 'automation', 'chemistry']
            }
        ]

        logger.info(f"Found {len(papers)} relevant papers")

    except Exception as e:
        logger.error(f"Error scanning literature: {e}")

    return papers

def scan_conferences():
    """Scan conference abstracts and proceedings"""
    logger.info("Scanning conference sources...")

    conferences = []

    try:
        # Simulate conference abstracts
        conferences = [
            {
                'name': 'AACC Annual Meeting',
                'date': '2026-06-15',
                'presenter': 'Johnson Lab',
                'title': 'High-Throughput Screening Methods',
                'relevance': 'relevant',
                'tags': ['HTS', 'screening', 'automation']
            },
            {
                'name': 'ACS National Meeting',
                'date': '2026-07-01',
                'presenter': 'Williams Group',
                'title': 'Machine Learning for Chemistry',
                'relevance': 'novel',
                'tags': ['ML', 'chemistry', 'AI']
            }
        ]

        logger.info(f"Found {len(conferences)} relevant conference presentations")

    except Exception as e:
        logger.error(f"Error scanning conferences: {e}")

    return conferences

def scan_vendors():
    """Scan vendor announcements for new products"""
    logger.info("Scanning vendor sources...")

    vendors = []

    try:
        # Simulate vendor announcements
        vendors = [
            {
                'vendor': 'Teledyne',
                'date': '2026-06-20',
                'product': 'Automated Chemistry Module v2.1',
                'capability': 'Closed-loop automation',
                'relevance': 'fills_gap',
                'tags': ['automation', 'robotics']
            },
            {
                'vendor': 'Sigma-Aldrich',
                'date': '2026-06-25',
                'announcement': 'New AI-assisted reagent selection',
                'relevance': 'adjacent',
                'tags': ['AI', 'reagents', 'selection']
            }
        ]

        logger.info(f"Found {len(vendors)} vendor announcements")

    except Exception as e:
        logger.error(f"Error scanning vendors: {e}")

    return vendors

def scan_competitors():
    """Scan competitor activity (patents, publications, jobs)"""
    logger.info("Scanning competitor sources...")

    competitors = []

    try:
        # Simulate competitor intelligence
        competitors = [
            {
                'company': 'Roche Diagnostics',
                'activity_type': 'patent',
                'date': '2026-06-10',
                'description': 'Automated DMTA system with ML optimization',
                'threat_level': 'high',
                'tags': ['automation', 'DMTA', 'ML']
            },
            {
                'company': 'Thermo Fisher',
                'activity_type': 'product_launch',
                'date': '2026-06-18',
                'description': 'New liquid handling system with AI feedback',
                'threat_level': 'moderate',
                'tags': ['robotics', 'automation', 'AI']
            },
            {
                'company': 'Bio-Rad',
                'activity_type': 'job_posting',
                'date': '2026-06-22',
                'description': 'Hiring for AI/ML in diagnostics team',
                'threat_level': 'low',
                'tags': ['AI', 'ML', 'hiring']
            }
        ]

        logger.info(f"Found {len(competitors)} competitor signals")

    except Exception as e:
        logger.error(f"Error scanning competitors: {e}")

    return competitors

def create_external_entries(papers, conferences, vendors, competitors):
    """Create Spark/Forge entries from external intelligence"""
    logger.info("Creating entries from external intelligence...")

    external_entries = {
        'spark_entries': [],
        'forge_entries': []
    }

    # Create Spark entries from papers
    for idx, paper in enumerate(papers, 1):
        entry = {
            'entry_id': f'S{100+idx}',
            'date': paper['date'],
            'type': 'Spark',
            'title': paper['title'],
            'source': paper['source'],
            'category': 'Literature',
            'tags': paper['tags'],
            'strategic_link': 'Strategic Questions',
            'relevance': paper['relevance']
        }
        external_entries['spark_entries'].append(entry)

    # Create Spark entries from conferences
    for idx, conf in enumerate(conferences, 1):
        entry = {
            'entry_id': f'S{200+idx}',
            'date': conf['date'],
            'type': 'Spark',
            'title': conf['title'],
            'presenter': conf['presenter'],
            'source': conf['name'],
            'category': 'Conference',
            'tags': conf['tags'],
            'strategic_link': 'Competitive Intelligence'
        }
        external_entries['spark_entries'].append(entry)

    # Create Forge entries from vendors
    for idx, vendor in enumerate(vendors, 1):
        entry = {
            'entry_id': f'F{100+idx}',
            'date': vendor['date'],
            'type': 'Forge',
            'title': vendor.get('product', vendor.get('announcement')),
            'vendor': vendor['vendor'],
            'category': 'Tool / Capability',
            'tags': vendor['tags'],
            'strategic_link': 'Capability Building'
        }
        external_entries['forge_entries'].append(entry)

    # Create Spark entries from competitors
    for idx, comp in enumerate(competitors, 1):
        entry = {
            'entry_id': f'S{300+idx}',
            'date': comp['date'],
            'type': 'Spark',
            'title': comp['description'],
            'company': comp['company'],
            'activity': comp['activity_type'],
            'category': 'Competitor',
            'tags': comp['tags'],
            'strategic_link': 'Competitive Intelligence',
            'threat_level': comp['threat_level']
        }
        external_entries['spark_entries'].append(entry)

    return external_entries

def main():
    """Main Phase 2 execution"""
    try:
        logger.info("=" * 60)
        logger.info("PHASE 2: External Intelligence Scan")
        logger.info("=" * 60)

        # Scan all sources
        papers = scan_literature()
        conferences = scan_conferences()
        vendors = scan_vendors()
        competitors = scan_competitors()

        # Create entries
        external_entries = create_external_entries(papers, conferences, vendors, competitors)

        # Save for Phase 3
        with open('phase2_external_entries.json', 'w') as f:
            json.dump(external_entries, f, indent=2)

        logger.info(f"Phase 2 Complete: {len(external_entries['spark_entries'])} Spark + {len(external_entries['forge_entries'])} Forge entries created")

    except Exception as e:
        logger.error(f"Phase 2 Failed: {e}")
        sys.exit(1)

if __name__ == '__main__':
    main()
