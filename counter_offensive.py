import time
import sys
import json
import random

def generate_fireworks_pattern():
    patterns = [
        r"""
          .     .
    .   .    .    .
  .  .    .  .
    .     .
.      .    .      .
        .
""",
        r"""
    \ /          .     .           \ /
. -- .     .   .    .   -- .    . -- .
    / \     .  .    .   / \
         .          .              .
""",
        r"""
    *
         .     .    .    .
  .   .    .  *  .
    .     .  .    .     .
  .    *     .  .  *
       .    .   *    .    *
    *    .     . .  *  .
.     .    *   .    .
""",
        r"""
       .      .      .  . .
   .     .      .   .    .
     .     .  .    .    .    .
      .    .     .    .
   .    .   .      .   .    .  .
.    .     .     .   .    .     .
   .    .     .     .    .
     .  .   .    .    .  .
       .    .   .   .
""",
    ]

    return random.choice(patterns)

def display_fireworks():
    fireworks = generate_fireworks_pattern()
    print("\033[93m" + fireworks + "\033[0m")
    time.sleep(1)

# ... Rest of the code remains unchanged ...


def generate_random_packet_details():
    source_ips = ["192.168.0.100", "10.0.0.2", "172.16.0.5", "10.20.30.40"]
    destination_ips = ["10.0.0.1", "172.16.0.10", "192.168.0.200", "8.8.8.8"]
    protocols = ["TCP", "UDP", "ICMP"]
    lengths = [random.randint(500, 2000), random.randint(300, 1000), random.randint(100, 500)]
    information = ["Normal traffic", "DDoS attack packets", "Suspicious activity"]
    tls_information = ["Not applicable", "TLS v1.2", "TLS v1.3"]

    return {
        "Source": random.choice(source_ips),
        "Destination": random.choice(destination_ips),
        "Protocol": random.choice(protocols),
        "Length": f"{random.choice(lengths)} bytes",
        "Information": random.choice(information),
        "TLS Information": random.choice(tls_information)
    }

def show_packet_details():
    packet_details = generate_random_packet_details()

    print("\n\033[1mPacket Details:\033[0m")
    for key, value in packet_details.items():
        print(f"\033[94m{key}:\033[0m {value}")

def main():
    with open("read.json") as file:
        countermeasures = json.load(file)

    print("===== DDoS Counter-Offensive Menu =====")
    for option in countermeasures:
        print(f"\033[94m{option}. \033[0m{countermeasures[option]['name']}")
    print("\033[91mq. Quit\033[0m")
    print("=======================================")

    while True:
        user_choice = input("\nEnter the number of your choice (or 'q' to quit): ")

        if user_choice.lower() == "q":
            print("Exiting...")
            break

        if user_choice in countermeasures:
            print(f"\n\033[1m{countermeasures[user_choice]['name']}:\033[0m {countermeasures[user_choice]['description']}")
            display_fireworks()
            choice = input("\nDo you want to see packet details? (yes/no): ").lower()
            if choice == 'yes':
                show_packet_details()
        else:
            print("\033[91mInvalid choice. Please enter a valid number.\033[0m")

if __name__ == "__main__":
    main()
