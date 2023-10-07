import time
import random
def generate_fireworks_pattern():
    patterns = [
        (r"""
 *         .   *  .  *
    .  * .    .    .
 * .  .    .  *.   *
    .     .*           *
.  *    .    .  *    *.
  *      .*  .  *
""", "\033[91m"),  # Red
        (r"""
    \ /     *    .     .   /     *   \ /
. -- .  *  .   .*   .   \./ .    . -- .
    / \     .  .    .   / \         /
   /  *\  .      *    /.       *    * .
""", "\033[93m"),  # Yellow
        (r"""
    *    .     .    .    .
  .   .    .  *  .
    .     .  .    .     .
  .    *     .  .  *
       .    .   *    .    *
    *    .     . .  *  .
.     .    *   .    .
""", "\033[92m"),  # Green
        (r"""
       .      .      .  . .
   .     .      .   .    .
     .     .  .    .    .    .
      .    .     .    .
   .    .   .      .   .    .  .
.    .     .     .   .    .     .
   .    .     .     .    .
     .  .   .    .    .  .
       .    .   .   .
""", "\033[96m"),  # Cyan
        (r"""
 *         .   *  .  *
    .  * .    .    .
 * .  .    .  *.   *
    .     .*           *
.  *    .    .  *    *.
  *      .*  .  *
""", "\033[95m"),  # Red
        (r"""
    \ /     *    .     .   /     *   \ /
. -- .  *  .   .*   .   \./ .    . -- .
    / \     .  .    .   / \         /
   /  *\  .      *    /.       *    * .
""", "\033[97m"),  # Yellow
        (r"""
    *    .     .    .    .
  .   .    .  *  .
    .     .  .    .     .
  .    *     .  .  *
       .    .   *    .    *
    *    .     . .  *  .
.     .    *   .    .
""", "\033[94m"),  # Green
        (r"""
       .      .      .  . .
   .     .      .   .    .
     .     .  .    .    .    .
      .    .     .    .
   .    .   .      .   .    .  .
.    .     .     .   .    .     .
   .    .     .     .    .
     .  .   .    .    .  .
       .    .   .   .
""", "\033[90m"),  # Cyan
    ]
    return random.choice(patterns)
def display_fireworks():
    fireworks, color_code = generate_fireworks_pattern()
    print(color_code + fireworks + "\033[0m")
    time.sleep(1)

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
    display_fireworks()
    print("\n\033[1mPacket Details:\033[0m")
    for key, value in packet_details.items():
        print(f"\033[94m{key}:\033[0m {value}")
while True:
    print("\033[1m----- DDoS Counter-Offensive Menu -----\033[0m")
    print("\033[94m1. Rate Limiting\033[0m")
    print("\033[93m2. Web Application Firewall (WAF)\033[0m")
    print("\033[92m3. Anomaly Detection\033[0m")
    print("\033[91m4. Cloud-Based DDoS Protection\033[0m")
    print("\033[95m5. Blackhole Routing\033[0m")
    print("\033[96m6. FTP Bounce Attack (Counter Measure)\033[0m")
    print("\033[97m7. Smurf Attack (Counter Measure)\033[0m")
    print("\033[91m8. TCP SYN Flood (Counter Measure)\033[0m")
    print("\033[92m9. DNS Amplification (Counter Measure)\033[0m")
    print("\033[93m10. TLS Mitigation\033[0m")
    print("\033[96mq. Quit\033[0m")
    print("\033[1m---------------------------------------\033[0m")
    user_choice = input("Enter the number of your choice (or 'q' to quit): ")
    if user_choice.lower() == "q":
        print("Exiting...")
        break
    elif user_choice == "1":
        print("\033[94mRate Limiting:\033[0m Rate limiting restricts the number of requests from a single IP address.")
        print("By setting a threshold, you can block or delay excessive requests from suspicious sources.")
        show_packet_details()
    elif user_choice == "2":
        print("\033[93mWeb Application Firewall (WAF):\033[0m A WAF can analyze incoming HTTP requests and filter out potentially malicious ones.")
        print("It helps protect the web server from common attack patterns and vulnerabilities.")
        show_packet_details()
    elif user_choice == "3":
        print("\033[92mAnomaly Detection:\033[0m Anomaly detection mechanisms can identify unusual traffic patterns.")
        print("It helps to detect DDoS attacks by monitoring traffic behavior and identifying deviations from normal traffic.")
        show_packet_details()
    elif user_choice == "4":
        print("\033[91mCloud-Based DDoS Protection:\033[0m Leveraging cloud-based DDoS protection services can offload attack traffic away from the target server.")
        print("Cloud providers have robust infrastructure to absorb and mitigate large-scale DDoS attacks.")
        show_packet_details()
    elif user_choice == "5":
        print("\033[95mBlackhole Routing:\033[0m In severe DDoS attacks, blackhole routing can be used to drop traffic to the target IP address.")
        print("This approach takes the target offline temporarily, preventing collateral damage to the rest of the network.")
        show_packet_details()
    elif user_choice == "6":
        print("\033[96mFTP Bounce Attack (Counter Measure):\033[0m Countermeasures for FTP bounce attack.")
        print("Description of countermeasure here.")
        show_packet_details()
    elif user_choice == "7":
        print("\033[97mSmurf Attack (Counter Measure):\033[0m Countermeasures for Smurf attack.")
        print("Description of countermeasure here.")
        show_packet_details()
    elif user_choice == "8":
        print("\033[91mTCP SYN Flood (Counter Measure):\033[0m Countermeasures for TCP SYN flood.")
        print("Description of countermeasure here.")
        show_packet_details()
    elif user_choice == "9":
        print("\033[92mDNS Amplification (Counter Measure):\033[0m Countermeasures for DNS amplification.")
        print("Description of countermeasure here.")
        show_packet_details()
    elif user_choice == "10":
        print("\033[93mTLS Mitigation:\033[0m Mitigating DDoS attacks targeting TLS.")
        print("Description of TLS mitigation here.")
        show_packet_details()
    else:
        print("\033[91mInvalid choice. Please enter a valid number.\033[0m")

   # display_fireworks()
    
if __name__ == "__main__":
    main()