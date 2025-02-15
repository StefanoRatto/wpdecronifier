import csv
from datetime import datetime
import os

class WPDecronifier:
    def save_progress(self, start_time: datetime):
        """Save current progress to results file."""
        try:
            # Always show progress summary, even if no results yet
            print("\n[+] Progress Summary (Interrupted):")
            print(f"    • Sites processed: {self.current_site}/{self.total_sites}")
            print(f"    • Vulnerable sites found: {self.vulnerable_count}")
            print(f"    • HackerOne program matches: {self.h1_matches_count}")
            print(f"    • Intigriti program matches: {self.intigriti_matches_count}")
            print(f"    • Other bug bounty programs found: {self.other_bb_count}")
            
            # Save results if we have any
            if self.results:
                # Save to results.csv (create new file)
                results_file = "results.csv"
                file_exists = os.path.exists(results_file)
                
                with open(results_file, 'w', newline='') as f:
                    writer = csv.DictWriter(f, fieldnames=['vulnerable_url', 'program_url', 'platform', 'checked_at'])
                    writer.writeheader()
                    writer.writerows(self.results)
                print(f"\n[+] Progress saved to {results_file}")
                
                if self.h1_matches_count > 0 or self.intigriti_matches_count > 0 or self.other_bb_count > 0:
                    print("\n[!] Bug Bounty Program Matches Found So Far:")
                    seen_matches = set()
                    for result in self.results:
                        match_key = f"{result['vulnerable_url']} → {result['program_url']} ({result['platform']})"
                        if match_key not in seen_matches:
                            seen_matches.add(match_key)
                            print(f"    • {match_key}")
            else:
                print("\n[-] No results to save yet")
            
        except Exception as e:
            print(f"\n[-] Error saving progress: {str(e)}")

    def scan_and_save(self):
        # Implementation of scan_and_save method
        pass

    def save_final_results(self):
        # Implementation of save_final_results method
        pass

    def run(self):
        # Implementation of run method
        pass

    def __init__(self):
        # Initialization code
        pass 