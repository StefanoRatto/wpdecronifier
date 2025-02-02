# WordPress Cron Exposure Scanner (WPDecronifier)

This utility scans for WordPress sites exposed to the internet and checks if they have exposed wp-cron.php endpoints that could be potential security issues. It then cross-references these sites with HackerOne's public bug bounty programs to identify if any vulnerable sites are in scope for responsible disclosure.

## Features

- Searches for WordPress sites using Shodan API (with pagination)
- Checks for exposed wp-cron.php endpoints (only considers 200 OK responses as vulnerable)
- Cross-references findings with HackerOne public programs (with pagination)
- Outputs results in CSV format with timestamped filenames
- Comprehensive logging with both console output and log files
- Reverse DNS lookups for IP addresses
- Cool ASCII art banner
- Environment variable validation
- Configurable result limits via command-line arguments

## Prerequisites

- Python 3.6 or higher
- Shodan API key (sign up at https://shodan.io)
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
# Shodan API Key (required)
export SHODAN_API_KEY='your-api-key-here'

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
2. Set up logging with timestamped filenames
3. Validate all required environment variables
4. Search for WordPress sites using Shodan (respecting the specified result limit)
5. Attempt to resolve domain names for IP addresses
6. Check each site for exposed wp-cron.php endpoints (only 200 OK responses)
7. Cross-reference findings with HackerOne programs
8. Save results to a timestamped CSV file

## Output Files

The script generates two types of output files:

1. Results CSV (`wpdecronifier_results_YYYYMMDD_HHMMSS_UTC.csv`):
   - vulnerable_url: The URL of the vulnerable WordPress site
   - hackerone_program: The URL of the corresponding HackerOne program
   - checked_at: Timestamp of when the check was performed

2. Execution Log (`wpdecronifier_execution_log_YYYYMMDD_HHMMSS_UTC.log`):
   - Complete execution log including all console output
   - Search progress and results
   - Error messages and warnings
   - Final summary

## Security Considerations

- This tool is intended for security research and responsible disclosure only
- Always ensure you have permission to scan target systems
- Follow responsible disclosure guidelines when reporting vulnerabilities
- Some sites may block automated scanning attempts
- Handle API credentials securely and never commit them to version control

## Limitations

- Relies on Shodan's database, which may not be completely up-to-date
- HackerOne API rate limits may apply
- Some sites may implement security measures that prevent scanning
- Only considers direct 200 OK responses as vulnerable (no redirect following)
- All environment variables (SHODAN_API_KEY, H1_TOKEN, H1_USERNAME) are required
- Shodan API query credits may limit the number of results

# Licensing

The tool is licensed under the [GNU General Public License](https://www.gnu.org/licenses/gpl-3.0.en.html).

# Legal disclaimer

Usage of this tool to interact with targets without prior mutual consent is illegal. It's the end user's responsibility to obey all applicable local, state and federal laws. Developers assume no liability and are not responsible for any misuse or damage caused by this program. Only use for educational purposes.regulations. 
