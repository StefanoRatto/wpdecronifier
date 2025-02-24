# WordPress Cron Exposure Scanner (wpdecronifier)

This utility scans for WordPress sites exposed to the internet and checks if they have exposed wp-cron.php endpoints that could be potential security issues. It then cross-references these sites with both HackerOne and Intigriti public bug bounty programs to identify if any vulnerable sites are in scope for responsible disclosure.

## Features

- Discovers WordPress sites using Common Crawl data:
  - Automatically fetches and uses the latest Common Crawl index
  - Fallback to recent stable index if latest is unavailable
  - Shows collection dates and index information
  - Smart caching of downloaded files
- Intelligent WordPress site validation with multiple indicators:
  - WordPress-specific headers
  - wp-content/wp-includes patterns
  - WordPress generator meta tags
  - wp-json API endpoint checks
- Smart domain matching with multiple variations for bug bounty scope comparison:
  - Original domain (e.g., `example.com`)
  - WWW prefix (e.g., `www.example.com`)
  - Parent domain for subdomains (e.g., `example.com` for `sub.example.com`)
  - All variations with and without WWW
  - Wildcard subdomain matching
  - Intelligent parent domain extraction
- Multi-platform bug bounty program integration:
  - HackerOne API with pagination (100 programs per page)
  - Intigriti API with pagination (50 programs per page)
  - Support for both URL and wildcard scope types
  - Proper handling of eligibility status
  - Graceful handling of rate limits with exponential backoff
  - Smart retry logic for API failures
  - Automatic skipping of disabled/private programs
- Performance optimizations:
  - Parallel processing of Common Crawl files
  - Local file caching to improve performance across runs
  - Configurable worker count for parallel processing
  - Rate limiting for API requests
  - API response caching with 24-hour validity
- Comprehensive vulnerability checking:
  - Direct wp-cron.php endpoint validation
  - Only considers 200 OK responses as vulnerable
  - No redirect following to avoid false positives
- Enhanced output and logging:
  - Unified logging with append mode for all scans
  - Detailed progress indicators
  - Single CSV output format:
    - All results saved to results.csv
    - Creates new file for each scan
  - Clear phase separation and progress tracking
  - Detailed matching information for each program
- Additional features:
  - Reverse DNS lookups for IP addresses
  - Cool ASCII art banner
  - Environment variable validation
  - Configurable result limits
  - SSL warning suppression for self-signed certificates
  - Alternative bug bounty program discovery
  - Web-based program searching

## Prerequisites

- Python 3.8 or higher
- HackerOne API credentials (username and token)
- Intigriti API token
- Internet connection for API access

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/wpdecronifier.git
cd wpdecronifier
```

2. Install required packages:
```bash
pip install -r requirements.txt
```

3. Set up environment variables:
```bash
export H1_TOKEN='your-hackerone-token'
export H1_USERNAME='your-hackerone-username'
export INTIGRITI_TOKEN='your-intigriti-token'
```

## Usage

Basic usage with default settings:
```bash
python wpdecronifier.py
```

Limit the number of WordPress sites to check:
```bash
python wpdecronifier.py 5  # Check only 5 sites
```

## Output Files

The tool generates two output files:

1. Results File:
   - File: `results.csv`
   - Contains scan results from the current run
   - Creates a new file for each scan
   - Previous results are overwritten

2. Log File:
   - File: `wpdecronifier.log`
   - Contains detailed execution logs
   - Appends logs from all runs

## CSV Format

The results.csv file contains the following columns:
- `vulnerable_url`: The URL of the vulnerable WordPress site
- `program_url`: The URL of the matching bug bounty program
- `platform`: The platform hosting the bug bounty program (HackerOne/Intigriti/Self-Hosted/etc.)
- `checked_at`: Timestamp of when the check was performed

## Rate Limiting

The tool implements smart rate limiting:
- Automatic handling of API rate limits
- Exponential backoff for rate-limited requests
- Configurable delays between requests
- Maximum retry attempts for failed requests

## Caching

Two types of caching are implemented:
1. API Response Cache:
   - 24-hour validity for bug bounty program data
   - Stored in `api_cache/` directory:
     - `hackerone_programs.json` for HackerOne programs
     - `intigriti_programs.json` for Intigriti programs
   - Direct program data caching without timestamp wrapping
   - Reduces API calls and improves performance
   - Automatic cache invalidation after 24 hours

2. Common Crawl Cache:
   - Stores downloaded Common Crawl files locally
   - Reused across multiple runs
   - Located in `commoncrawl_cache/` directory

## Error Handling

The tool gracefully handles various error conditions:
- API rate limits with automatic retries
- Network connectivity issues
- Invalid API credentials
- Missing environment variables
- Malformed API responses
- Program 404 errors (disabled/private programs)

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Disclaimer

This tool is intended for security researchers and bug bounty hunters. Always ensure you have permission to test any target systems and comply with the scope and rules of bug bounty programs.

## Workflow

The tool operates in three phases:

1. WordPress Site Discovery:
   - Fetches latest Common Crawl index information
   - Downloads and processes Common Crawl data files
   - Uses parallel processing for faster discovery
   - Validates potential WordPress sites
   - Respects the specified result limit

2. Bug Bounty Program Fetching:
   - Retrieves programs from HackerOne (paginated, 100 per page)
   - Retrieves programs from Intigriti (paginated, 50 per page)
   - Handles rate limiting and pagination automatically
   - Processes only active/open programs

3. Vulnerability Checking:
   - Tests wp-cron.php exposure
   - Matches vulnerable sites against program scopes
   - Generates detailed output for matches

## Security Considerations

- This tool is intended for security research and responsible disclosure only
- Always ensure you have permission to scan target systems
- Follow responsible disclosure guidelines when reporting vulnerabilities
- Some sites may block automated scanning attempts
- Handle API credentials securely and never commit them to version control
- The tool respects rate limits for both HackerOne and Intigriti APIs

## Limitations

- Common Crawl data may not be completely up-to-date (but uses latest available index)
- HackerOne API rate limits (Enterprise: 10k/day, default: 3.6k/day)
- Intigriti API rate limits (standard limits apply)
- Only considers direct 200 OK responses as vulnerable
- All environment variables (H1_TOKEN, H1_USERNAME, INTIGRITI_TOKEN) are required
- Some sites may implement security measures that prevent scanning

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Licensing

The tool is licensed under the [GNU General Public License](https://www.gnu.org/licenses/gpl-3.0.en.html).

## Legal disclaimer

Usage of this tool to interact with targets without prior mutual consent is illegal. It's the end user's responsibility to obey all applicable local, state and federal laws. Developers assume no liability and are not responsible for any misuse or damage caused by this program. Only use for educational purposes.regulations. 
