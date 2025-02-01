# WordPress Cron Exposure Scanner (WPDecronifier)

This utility scans for WordPress sites exposed to the internet and checks if they have exposed wp-cron.php endpoints that could be potential security issues. It then cross-references these sites with HackerOne's public bug bounty programs to identify if any vulnerable sites are in scope for responsible disclosure.

## Features

- Searches for WordPress sites using Shodan API
- Checks for exposed wp-cron.php endpoints
- Cross-references findings with HackerOne public programs
- Outputs results in CSV format
- Multi-threaded scanning for improved performance
- SSL verification disabled to handle self-signed certificates
- Live progress tracking with timestamps
- Cool ASCII art banner
- HackerOne API authentication support

## Prerequisites

- Python 3.6 or higher
- Shodan API key (sign up at https://shodan.io)
- HackerOne account and API token (for program matching)

## Installation

1. Clone this repository:
```bash
git clone https://github.com/yourusername/wpdecronifier.git
cd wpdecronifier
```

2. Install required dependencies:
```bash
pip install -r requirements.txt
```

3. Set up your API credentials as environment variables:

For Shodan (required):
```bash
export SHODAN_API_KEY='your-api-key-here'
```

For HackerOne (optional, but recommended for program matching):
```bash
export H1_API_TOKEN='your-api-token-here'
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
```bash
./wpdecronifier
```

The script will:
1. Display a cool ASCII art banner
2. Search for WordPress sites using Shodan
3. Check each site for exposed wp-cron.php endpoints
4. Cross-reference findings with HackerOne programs (if credentials are provided)
5. Save results to `results.csv`

## Output

The script generates a CSV file (`results.csv`) with the following columns:
- WordPress Site: The URL of the WordPress site with exposed wp-cron.php
- HackerOne Program: The URL of the corresponding HackerOne program

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
- False positives may occur
- HackerOne program matching requires valid API credentials

## Contributing

Feel free to submit issues, fork the repository, and create pull requests for any improvements.

## Licensing

The tool is licensed under the [GNU General Public License](https://www.gnu.org/licenses/gpl-3.0.en.html).

## Legal disclaimer

Usage of this tool to interact with targets without prior mutual consent is illegal. It's the end user's responsibility to obey all applicable local, state and federal laws. Developers assume no liability and are not responsible for any misuse or damage caused by this program. Only use for educational purposes.
