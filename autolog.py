#!/usr/bin/env python3
import os
from datetime import datetime
from typing import Optional, Tuple
from dataclasses import dataclass
from urllib.parse import urlparse

LOG_FILE: str = "log.md"
DATE_FORMAT: str = "%Y-%m-%d"


@dataclass
class LogEntry:
    entry_type: str
    name: str
    language: str
    link: str
    description: str


def init_log_file() -> None:
    """Initialize the log file with headers if it doesn't already exist."""
    if not os.path.exists(LOG_FILE):
        with open(LOG_FILE, "w") as f:
            f.write(
                "| S.No | Date       | Type    | Name              | Language | Link                                   | Website   | Description                        |\n"
            )
            f.write(
                "|------|------------|---------|-------------------|----------|----------------------------------------|-----------|------------------------------------|\n"
            )


def get_last_entry_details() -> Tuple[Optional[int], Optional[str]]:
    """Get the last serial number and date from the log file.

    Returns:
        Tuple[Optional[int], Optional[str]]: The last serial number and date, or None if the file is empty.
    """
    if not os.path.exists(LOG_FILE):
        return None, None

    with open(LOG_FILE, "r") as f:
        lines = f.readlines()
        if len(lines) <= 2:
            return None, None

        # Find the last entry that has a serial number
        for line in reversed(lines[2:]):
            parts = line.split("|")
            last_serial = parts[1].strip()
            last_date = parts[2].strip()
            if last_serial:
                return int(last_serial), last_date
        return None, last_date


def extract_website_name(url: str) -> str:
    """Extract the website name from a URL."""
    parsed_url = urlparse(url)
    if parsed_url.scheme and parsed_url.netloc:
        return parsed_url.netloc.split(".")[0]
    return ""


def log_entry(
    f, entry: LogEntry, last_serial: Optional[int], last_date: Optional[str]
) -> None:
    """Log an entry to the log file.

    Args:
        f (file object): The file object to write to.
        entry (LogEntry): The log entry to be added.
        last_serial (Optional[int]): The last serial number.
        last_date (Optional[str]): The last date.
    """
    entry_date = datetime.now()
    entry_date_str = entry_date.strftime(DATE_FORMAT)

    # Check if the last entry has the same date as the current entry
    if last_date == entry_date_str:
        serial_number = ""
    else:
        if entry.entry_type.lower() != "update":
            # Increment serial number only for new entries
            serial_number = str((last_serial or 0) + 1).rjust(4)
        else:
            serial_number = ""

    website_name = extract_website_name(entry.link)

    log_line = "| {0} | {1} | {2:<7} | {3:<17} | {4:<8} | [Link]({5}) | {6:<9} | {7:<34} |\n".format(
        serial_number,
        entry_date_str,
        entry.entry_type.capitalize(),
        entry.name,
        entry.language,
        entry.link,
        website_name,
        entry.description,
    )

    f.write(log_line)


def log_update(entry: LogEntry) -> None:
    """Log an update entry below the last matching name and link in the log file."""
    temp_file = "temp.md"
    with open(LOG_FILE, "r") as f, open(temp_file, "w") as temp_f:
        lines = f.readlines()
        temp_f.writelines(lines[:2])  # Write the header to the temp file

        # Find the last matching entry
        inserted = False
        for i, line in enumerate(lines[2:], start=2):
            temp_f.write(line)
            parts = line.split("|")
            if (
                parts[4].strip() == entry.name
                and parts[6].strip() == f"[Link]({entry.link})"
            ):
                # Insert the update entry below the matching entry
                temp_f.write(
                    "|      | {0} | {1:<7} | {2:<17} | {3:<8} | [Link]({4}) | {5:<9} | {6:<34} |\n".format(
                        datetime.now().strftime(DATE_FORMAT),
                        entry.entry_type.capitalize(),
                        entry.name,
                        entry.language,
                        entry.link,
                        extract_website_name(entry.link),
                        entry.description,
                    )
                )
                inserted = True

        if not inserted:
            temp_f.write(
                "|      | {0} | {1:<7} | {2:<17} | {3:<8} | [Link]({4}) | {5:<9} | {6:<34} |\n".format(
                    datetime.now().strftime(DATE_FORMAT),
                    entry.entry_type.capitalize(),
                    entry.name,
                    entry.language,
                    entry.link,
                    extract_website_name(entry.link),
                    entry.description,
                )
            )

    os.replace(temp_file, LOG_FILE)


def main() -> None:
    """Main function to run the logging script."""
    init_log_file()

    try:
        while True:
            while True:
                entry_type: str = (
                    input("Enter the entry type (new|n/update|u): ").strip().lower()
                )
                if entry_type in ["new", "n"]:
                    entry_type = "new"
                    break
                elif entry_type in ["update", "u"]:
                    entry_type = "update"
                    break
                else:
                    print(
                        "Invalid entry type. Please enter 'new', 'n' or 'update', 'u'."
                    )

            name: str = input("Enter the name: ").strip().lower()
            language: str = input("Enter the language: ").strip().capitalize()
            link: str = input("Enter the link: ").strip()
            description: str = input("Enter the description: ").strip().lower()
            entry = LogEntry(entry_type, name, language, link, description)

            if entry_type == "new":
                last_serial, last_date = get_last_entry_details()
                with open(LOG_FILE, "a") as f:
                    log_entry(f, entry, last_serial, last_date)
            else:
                log_update(entry)

            another: str = (
                input("Do you want to log another entry? (yes|y|enter/no|n): ")
                .strip()
                .lower()
            )
            if another not in ["yes", "y", ""]:
                break

    except KeyboardInterrupt:
        print("\nExiting...")


if __name__ == "__main__":
    main()
