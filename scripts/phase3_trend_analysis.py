#!/usr/bin/env python3
"""
Phase 3: Trend Analysis & RED/YELLOW/GREEN Flagging
Analyzes convergence signals and flags urgent items
"""

import os
import sys
import json
import logging
from collections import Counter
from pathlib import Path
from dotenv import load_dotenv

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('logs/phase3_trend_analysis.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

load_dotenv()

def load_all_entries():
    """Load entries from Phase 1 and Phase 2"""
    logger.info("Loading all entries...")

    all_entries = {
        'spark_entries': [],
        'forge_entries': []
    }

    try:
        # Load Phase 1 entries
        if Path('phase1_extracted_entries.json').exists():
            with open('phase1_extracted_entries.json', 'r') as f:
                phase1 = json.load(f)
                all_entries['spark_entries'].extend(phase1.get('spark_entries', []))
                all_entries['forge_entries'].extend(phase1.get('forge_entries', []))

        # Load Phase 2 entries
        if Path('phase2_external_entries.json').exists():
            with open('phase2_external_entries.json', 'r') as f:
                phase2 = json.load(f)
                all_entries['spark_entries'].extend(phase2.get('spark_entries', []))
                all_entries['forge_entries'].extend(phase2.get('forge_entries', []))

        logger.info(f"Loaded {len(all_entries['spark_entries'])} Spark + {len(all_entries['forge_entries'])} Forge entries")

    except Exception as e:
        logger.error(f"Error loading entries: {e}")

    return all_entries

def analyze_tags(entries):
    """Analyze tag frequency across all entries"""
    logger.info("Analyzing tag frequency...")

    all_tags = []
    for entry in entries:
        all_tags.extend(entry.get('tags', []))

    tag_frequency = Counter(all_tags)
    return tag_frequency

def score_convergence(entries):
    """Score convergence signals (RED/YELLOW/GREEN)"""
    logger.info("Scoring convergence signals...")

    signals = {}

    # Count source types for each tag
    tag_sources = {}
    for entry in entries:
        tags = entry.get('tags', [])
        source = entry.get('category', 'unknown')

        for tag in tags:
            if tag not in tag_sources:
                tag_sources[tag] = []
            tag_sources[tag].append(source)

    # Score each theme
    for tag, sources in tag_sources.items():
        unique_sources = len(set(sources))
        frequency = len(sources)

        # Calculate convergence score
        score = unique_sources  # How many different sources mention this

        # Determine flag
        if score >= 4:  # 4+ sources converging
            flag = '🔴 RED'
            confidence = 'HIGH'
        elif score >= 2:  # 2-3 sources
            flag = '🟡 YELLOW'
            confidence = 'MODERATE'
        else:  # Single source
            flag = '🟢 GREEN'
            confidence = 'LOW'

        signals[tag] = {
            'score': score,
            'frequency': frequency,
            'sources': list(set(sources)),
            'flag': flag,
            'confidence': confidence
        }

    return signals

def create_analysis_report(tag_frequency, signals):
    """Create the trend analysis report"""
    logger.info("Creating analysis report...")

    report = {
        'timestamp': str(Path('phase1_extracted_entries.json').stat().st_mtime) if Path('phase1_extracted_entries.json').exists() else '',
        'tag_frequency': dict(tag_frequency.most_common(20)),
        'convergence_signals': signals,
        'red_flags': [tag for tag, sig in signals.items() if sig['flag'].startswith('🔴')],
        'yellow_signals': [tag for tag, sig in signals.items() if sig['flag'].startswith('🟡')],
        'green_signals': [tag for tag, sig in signals.items() if sig['flag'].startswith('🟢')]
    }

    return report

def main():
    """Main Phase 3 execution"""
    try:
        logger.info("=" * 60)
        logger.info("PHASE 3: Trend Analysis & Flagging")
        logger.info("=" * 60)

        # Load all entries
        all_entries = load_all_entries()
        all_spark = all_entries['spark_entries']
        all_forge = all_entries['forge_entries']

        # Analyze tags
        tag_frequency = analyze_tags(all_spark + all_forge)

        # Score convergence
        signals = score_convergence(all_spark + all_forge)

        # Create report
        analysis = create_analysis_report(tag_frequency, signals)

        # Save analysis
        with open('phase3_analysis.json', 'w') as f:
            json.dump(analysis, f, indent=2)

        logger.info(f"Analysis Complete:")
        logger.info(f"  - Red flags: {len(analysis['red_flags'])}")
        logger.info(f"  - Yellow signals: {len(analysis['yellow_signals'])}")
        logger.info(f"  - Green signals: {len(analysis['green_signals'])}")

    except Exception as e:
        logger.error(f"Phase 3 Failed: {e}")
        sys.exit(1)

if __name__ == '__main__':
    main()
