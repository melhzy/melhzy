#!/usr/bin/env python3
"""
Update Google Scholar citation data and generate visualization chart.
"""

import json
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')  # Use non-interactive backend
import numpy as np
from pathlib import Path

# Try to import scholarly, fall back to manual data entry if not available
try:
    from scholarly import scholarly
    USE_SCHOLARLY = True
except ImportError:
    USE_SCHOLARLY = False
    print("Warning: scholarly library not available. Using manual data entry.")

# Google Scholar user ID
SCHOLAR_ID = "WgqFSKUAAAAJ"

def fetch_scholar_data():
    """Fetch citation data from Google Scholar."""
    if USE_SCHOLARLY:
        try:
            # Search for author
            search_query = scholarly.search_author_id(SCHOLAR_ID)
            author = scholarly.fill(search_query)
            
            # Extract citation data
            citations_per_year = author.get('cites_per_year', {})
            total_citations = author.get('citedby', 0)
            hindex = author.get('hindex', 0)
            i10index = author.get('i10index', 0)
            
            return {
                'citedby': str(total_citations),
                'hindex': str(hindex),
                'i10index': str(i10index),
                'citations_per_year': citations_per_year
            }
        except Exception as e:
            print(f"Error fetching from Google Scholar: {e}")
            return None
    return None

def load_or_create_default_data():
    """Load existing data or create default structure."""
    citations_file = Path('citations.json')
    
    if citations_file.exists():
        with open(citations_file, 'r') as f:
            data = json.load(f)
    else:
        # Default data structure with sample yearly citations
        data = {
            'citedby': '120',
            'hindex': '6',
            'i10index': '4',
            'citations_per_year': {
                '2020': 5,
                '2021': 12,
                '2022': 18,
                '2023': 28,
                '2024': 35,
                '2025': 22
            }
        }
    
    return data

def generate_citation_chart(data):
    """Generate SVG chart showing citations over years."""
    citations_per_year = data.get('citations_per_year', {})
    
    if not citations_per_year:
        print("No citation data available for chart generation")
        return
    
    # Sort years
    years = sorted(citations_per_year.keys())
    citations = [citations_per_year[year] for year in years]
    
    # Create figure with custom styling
    fig, ax = plt.subplots(figsize=(10, 5), dpi=100)
    fig.patch.set_facecolor('#ffffff')
    ax.set_facecolor('#ffffff')
    
    # Create bar chart
    bars = ax.bar(years, citations, color='#4285F4', alpha=0.8, edgecolor='#1a73e8', linewidth=1.5)
    
    # Customize appearance
    ax.set_xlabel('Year', fontsize=12, fontweight='bold', color='#333333')
    ax.set_ylabel('Citations', fontsize=12, fontweight='bold', color='#333333')
    ax.set_title('Citations Per Year', fontsize=14, fontweight='bold', color='#333333', pad=20)
    
    # Add value labels on bars
    for bar in bars:
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2., height,
                f'{int(height)}',
                ha='center', va='bottom', fontsize=10, fontweight='bold', color='#333333')
    
    # Style the grid
    ax.grid(axis='y', alpha=0.3, linestyle='--', linewidth=0.5)
    ax.set_axisbelow(True)
    
    # Remove top and right spines
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_color('#CCCCCC')
    ax.spines['bottom'].set_color('#CCCCCC')
    
    # Adjust tick parameters
    ax.tick_params(colors='#666666', which='both')
    
    # Set y-axis to start at 0
    ax.set_ylim(bottom=0, top=max(citations) * 1.15)
    
    # Add total citations text
    total = sum(citations)
    ax.text(0.98, 0.98, f'Total: {total}', 
            transform=ax.transAxes, 
            fontsize=11, 
            fontweight='bold',
            color='#4285F4',
            ha='right', 
            va='top',
            bbox=dict(boxstyle='round,pad=0.5', facecolor='white', edgecolor='#4285F4', linewidth=1.5))
    
    plt.tight_layout()
    
    # Save as SVG
    plt.savefig('citations_chart.svg', format='svg', bbox_inches='tight', 
                facecolor='white', edgecolor='none')
    print("Citation chart generated: citations_chart.svg")
    plt.close()

def main():
    """Main execution function."""
    print("Updating Google Scholar citation data...")
    
    # Try to fetch fresh data from Google Scholar
    scholar_data = fetch_scholar_data()
    
    if scholar_data:
        print(f"Successfully fetched data from Google Scholar")
        print(f"Total Citations: {scholar_data['citedby']}")
        print(f"h-index: {scholar_data['hindex']}")
        print(f"i10-index: {scholar_data['i10index']}")
        data = scholar_data
    else:
        print("Using existing or default data")
        data = load_or_create_default_data()
    
    # Save citations data
    with open('citations.json', 'w') as f:
        json.dump(data, f, indent=2)
    print("Updated citations.json")
    
    # Generate chart
    generate_citation_chart(data)
    print("Citation data update complete!")

if __name__ == '__main__':
    main()
