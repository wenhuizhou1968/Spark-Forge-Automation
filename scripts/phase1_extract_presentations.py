#!/usr/bin/env python3
"""
Phase 1: Extract R&D Presentations
Extracts presentations from Z:\R&D\R&D Meeting\ folder
Identifies Spark (S###) and Forge (F###) topics
"""

import os
import sys
import json
import logging
from datetime import datetime, timedelta
from pathlib import Path
from dotenv import load_dotenv

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('logs/phase1_extraction.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

# Load environment variables
load_dotenv()
R_AND_D_PATH = os.getenv('R_AND_D_PATH', r'Z:\R&D\R&D Meeting')
SPARK_FORGE_PATH = os.getenv('SPARK_FORGE_PATH', r'Z:\R&D\R&D Meeting\AI-Spark-Forge')

def find_recent_presentations(days=14):
    """Find presentations from past N days"""
    logger.info(f"Searching for presentations from past {days} days...")

    presentations = []
    cutoff_date = datetime.now() - timedelta(days=days)

    try:
        # Search in Meetings folders
        meetings_path = Path(R_AND_D_PATH) / 'Meetings 2007'

        if meetings_path.exists():
            for pptx_file in meetings_path.rglob('*.pptx'):
                file_mtime = datetime.fromtimestamp(pptx_file.stat().st_mtime)
                if file_mtime >= cutoff_date:
                    presentations.append({
                        'path': str(pptx_file),
                        'name': pptx_file.name,
                        'date': file_mtime.strftime('%Y-%m-%d'),
                        'size': pptx_file.stat().st_size
                    })

            logger.info(f"Found {len(presentations)} presentations from past {days} days")
        else:
            logger.warning(f"Meetings folder not found: {meetings_path}")

    except Exception as e:
        logger.error(f"Error searching for presentations: {e}")
        return []

    return presentations

def extract_presentation_topics(presentation_path):
    """
    Extract topics from presentation
    Returns: {'spark_topics': [], 'forge_topics': []}
    """
    logger.info(f"Extracting topics from: {presentation_path}")

    # TODO: Implement actual extraction logic
    # For now, return template structure
    topics = {
        'spark_topics': [
            {
                'title': 'Strategic Insight',
                'description': 'Extract strategic insights and cross-domain connections',
                'tags': ['ai', 'chemistry', 'automation'],
                'category': 'AI / Chemistry'
            }
        ],
        'forge_topics': [
            {
                'title': 'Practical Method',
                'description': 'Extract methods, tools, and techniques',
                'tags': ['method', 'technique', 'workflow'],
                'category': 'Synthetic Method'
            }
        ]
    }

    return topics

def create_entries(presentations):
    """Create S### and F### entries from presentations"""
    logger.info(f"Creating entries for {len(presentations)} presentations...")

    entries = {
        'spark_entries': [],
        'forge_entries': []
    }

    for idx, pres in enumerate(presentations, 1):
        topics = extract_presentation_topics(pres['path'])

        # Create Spark entries
        for spark_topic in topics['spark_topics']:
            entry = {
                'entry_id': f'S{str(idx).zfill(3)}',
                'date': pres['date'],
                'type': 'Spark',
                'title': spark_topic['title'],
                'presenter': pres['name'].replace('.pptx', ''),
                'category': spark_topic['category'],
                'tags': spark_topic['tags'],
                'strategic_link': 'Strategic Questions',
                'source': pres['path']
            }
            entries['spark_entries'].append(entry)

        # Create Forge entries
        for forge_topic in topics['forge_topics']:
            entry = {
                'entry_id': f'F{str(idx).zfill(3)}',
                'date': pres['date'],
                'type': 'Forge',
                'title': forge_topic['title'],
                'presenter': pres['name'].replace('.pptx', ''),
                'category': forge_topic['category'],
                'tags': forge_topic['tags'],
                'strategic_link': 'Capability Building',
                'source': pres['path']
            }
            entries['forge_entries'].append(entry)

    return entries

def save_entries(entries):
    """Save extracted entries to JSON for next phases"""
    output_file = 'phase1_extracted_entries.json'

    with open(output_file, 'w') as f:
        json.dump(entries, f, indent=2)

    logger.info(f"Saved {len(entries['spark_entries'])} Spark + {len(entries['forge_entries'])} Forge entries to {output_file}")
    return output_file

def main():
    """Main Phase 1 execution"""
    try:
        logger.info("=" * 60)
        logger.info("PHASE 1: Extract R&D Presentations")
        logger.info("=" * 60)

        # Find recent presentations
        presentations = find_recent_presentations(days=14)

        if not presentations:
            logger.warning("No recent presentations found")
            return

        # Extract topics
        entries = create_entries(presentations)

        # Save for next phases
        save_entries(entries)

        logger.info("Phase 1 Complete ✓")

    except Exception as e:
        logger.error(f"Phase 1 Failed: {e}")
        sys.exit(1)

if __name__ == '__main__':
    main()
