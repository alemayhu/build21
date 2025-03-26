from pelican import signals
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime, timedelta
import os

def generate_contribution_graph(generator):
    # Create output directory for images if it doesn't exist
    output_path = os.path.join(generator.output_path, 'images')
    os.makedirs(output_path, exist_ok=True)
    
    # Collect article dates
    dates = [article.date for article in generator.articles]
    
    if not dates:
        return
    
    # Set up the plot with a style similar to GitHub
    plt.style.use('dark_background')
    fig, ax = plt.subplots(figsize=(12, 2))
    
    # Calculate date range (last year)
    end_date = max(dates)
    start_date = end_date - timedelta(days=365)
    
    # Create a date range for the x-axis
    date_range = [start_date + timedelta(days=x) for x in range(366)]
    
    # Count articles per day
    contributions = {}
    for date in dates:
        if date >= start_date:
            key = date.date()
            contributions[key] = contributions.get(key, 0) + 1
    
    # Create scatter plot data
    x_data = []
    y_data = []
    colors = []
    sizes = []
    
    for date in date_range:
        date = date.date()
        count = contributions.get(date, 0)
        if count > 0:
            x_data.append(date)
            y_data.append(0)  # All points on same y-level
            colors.append('#5397f5')  # Use the theme blue color
            sizes.append(100 + (count - 1) * 50)  # Bigger dots for more posts
    
    # Create the scatter plot
    if x_data:
        plt.scatter(x_data, y_data, c=colors, s=sizes, alpha=0.6)
    
    # Customize the plot
    ax.xaxis.set_major_locator(mdates.MonthLocator())
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%b'))
    
    # Remove y-axis and spines
    ax.set_yticks([])
    for spine in ax.spines.values():
        spine.set_visible(False)
    
    # Set background color
    fig.patch.set_facecolor('#ffffff')
    ax.set_facecolor('#ffffff')
    
    # Add grid for months
    ax.grid(True, axis='x', linestyle='-', alpha=0.1)
    
    # Adjust layout and save
    plt.tight_layout()
    output_file = os.path.join(output_path, 'contribution_graph.png')
    plt.savefig(output_file, dpi=150, bbox_inches='tight', facecolor='white')
    plt.close()
    
    # Add the image URL to the generator context
    generator.context['contribution_graph'] = 'images/contribution_graph.png'

def register():
    signals.article_generator_finalized.connect(generate_contribution_graph)
