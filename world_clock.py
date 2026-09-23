#!/usr/bin/env python3
"""
world-clock-cli — Global timezone converter and distributed team meeting scheduler.
"""
from datetime import datetime, timezone, timedelta

ZONES = {
    "San Francisco (PST/PDT)": -7,
    "New York (EST/EDT)":       -4,
    "London (UTC/BST)":          1,
    "Berlin (CET/CEST)":         2,
    "Tokyo (JST)":               9,
    "Sydney (AEST)":            10,
    "São Paulo (BRT)":          -3,
}

def get_zone_times() -> list[dict]:
    utc_now = datetime.now(timezone.utc)
    results = []
    for city, offset in ZONES.items():
        local_time = utc_now + timedelta(hours=offset)
        is_business = 9 <= local_time.hour < 18
        results.append({
            "city": city,
            "time_str": local_time.strftime("%Y-%m-%d %I:%M %p"),
            "hour": local_time.hour,
            "status": "🟢 Active Hours" if is_business else "🌙 Off Hours"
        })
    return results

def print_matrix():
    rows = get_zone_times()
    print("=" * 65)
    print("  Global Team Timezone Overview")
    print("=" * 65)
    print(f" {'Location':<28} | {'Local Time':<20} | {'Status'}")
    print("-" * 65)
    for r in rows:
        print(f" {r['city']:<28} | {r['time_str']:<20} | {r['status']}")
    print("=" * 65)

if __name__ == "__main__":
    print_matrix()
