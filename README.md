# WordPress Cron Exposure Scanner (WPDecronifier)

This utility scans for WordPress sites exposed to the internet and checks if they have exposed wp-cron.php endpoints that could be potential security issues. It then cross-references these sites with HackerOne's public bug bounty programs to identify if any vulnerable sites are in scope for responsible disclosure.

## Features

- Discovers WordPress sites using Common Crawl data (no Shodan API required)
- Intelligent WordPress site validation with multiple indicators
- Smart domain matching with multiple variations for HackerOne scope comparison
- Parallel processing of Common Crawl files for faster discovery
- Local file caching to improve performance across runs
- Checks for exposed wp-cron.php endpoints (only considers 200 OK responses as vulnerable)
- Cross-references findings with HackerOne public programs (with pagination)
- Outputs results in CSV format with timestamped filenames
- Unified logging with append mode for tracking all scans in a single file
- Reverse DNS lookups for IP addresses
- Cool ASCII art banner
- Environment variable validation
- Configurable result limits via command-line arguments

## Prerequisites

- Python 3.6 or higher
- HackerOne account and API token (required for program matching)

## Installation

1. Clone this repository:
```bash
git clone https://github.com/yourusername/wpdecronifier.git
cd wpdecronifier
```

2. Create and activate a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install required dependencies:
```bash
pip install -r requirements.txt
```

4. Set up your API credentials as environment variables:

```bash
# HackerOne credentials (required)
export H1_TOKEN='your-api-token-here'
export H1_USERNAME='your-username-here'
```

To get your HackerOne API token:
1. Log in to your HackerOne account
2. Go to Settings > API tokens
3. Generate a new API token with appropriate permissions

## Usage

Make the script executable:
```bash
chmod +x wpdecronifier
```

Run the script:

1. Without arguments (unlimited results):
```bash
./wpdecronifier
```

2. With a result limit (e.g., first 100 results):
```bash
./wpdecronifier 100
```

The script will:
1. Display a cool ASCII art banner
2. Set up logging (appending to wpdecronifier.log)
3. Validate all required environment variables
4. Search for WordPress sites using Common Crawl data (respecting the specified result limit)
5. Cache downloaded Common Crawl files for future use
6. Validate discovered sites using multiple WordPress indicators
7. Check each site for exposed wp-cron.php endpoints (only 200 OK responses)
8. Cross-reference findings with HackerOne programs using smart domain matching
9. Save results to a timestamped CSV file

## Output Files

The script generates two types of output files:

1. Results CSV (`wpdecronifier_results_YYYYMMDD_HHMMSS_UTC.csv`):
   - vulnerable_url: The URL of the vulnerable WordPress site
   - hackerone_program: The URL of the corresponding HackerOne program
   - checked_at: Timestamp of when the check was performed

2. Unified Log File (`wpdecronifier.log`):
   - Complete execution log for all scans
   - Clear separation between different scan sessions
   - Search progress and results
   - Error messages and warnings
   - Final summaries

## Smart Domain Matching

The tool now includes intelligent domain matching when comparing WordPress sites against HackerOne program scopes:

- Original domain (e.g., `example.com`)
- With www prefix (e.g., `www.example.com`)
- Subdomain variations (e.g., for `sub.example.com` it also checks `example.com`)
- Case-insensitive matching
- Normalized domain comparison (removing `www.` and `*.` prefixes)
- Exact match and suffix matching support

## Caching and Performance

- Common Crawl files are cached locally in the `commoncrawl_cache` directory
- Cached files are reused across runs to improve performance
- Parallel processing of Common Crawl files with configurable worker count
- Progress indicators showing processing speed and completion percentage

## Security Considerations

- This tool is intended for security research and responsible disclosure only
- Always ensure you have permission to scan target systems
- Follow responsible disclosure guidelines when reporting vulnerabilities
- Some sites may block automated scanning attempts
- Handle API credentials securely and never commit them to version control

## Limitations

- Common Crawl data may not be completely up-to-date
- HackerOne API rate limits may apply
- Some sites may implement security measures that prevent scanning
- Only considers direct 200 OK responses as vulnerable (no redirect following)
- HackerOne credentials (H1_TOKEN, H1_USERNAME) are required

## Contributing

Feel free to submit issues, fork the repository, and create pull requests for any improvements.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Disclaimer

This tool is for educational and research purposes only. Users are responsible for ensuring they have permission to scan target systems and comply with all applicable laws and regulations. 