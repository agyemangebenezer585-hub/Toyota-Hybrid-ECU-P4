# TOYOTA HYBRID P4 - ENGINE + MOTOR COMBINE
# Ebenezer - Ghana to Japan
# MEXT Project

print("=== TOYOTA HYBRID P4 - ENGINE + MOTOR COMBINE ===")

# Settings
LOW_SOC = 35
HIGH_SOC = 70
POWER_HIGH = 80  # High power demand

def hybrid_control(soc, power_demand):
    print(f"\n--- SOC: {soc}% | Power Demand: {power_demand}% ---")
    
    if soc < LOW_SOC:
        print("MODE: ENGINE ONLY - Battery LOW!")
        print("-> Engine ON, Charging Battery + Driving Wheels")
        print("-> Motor OFF - Protect Battery")
        
    elif soc >= LOW_SOC and soc <= HIGH_SOC:
        if power_demand > POWER_HIGH:
            print("MODE: HYBRID POWER - Engine + Motor!")
            print("-> Engine ON + Motor ON = Full Power!")
            print("-> For Acceleration / Hill Climb")
        else:
            print("MODE: NORMAL HYBRID - Efficient Drive")
            print("-> Engine ON, Motor Assist")
            
    elif soc > HIGH_SOC:
        if power_demand < 50:
            print("MODE: EV MODE - Electric Only!")
            print("-> Engine OFF, Motor ON - Silent & Clean!")
            print("-> Battery 70% -> 75% with Regen")
        else:
            print("MODE: EV + ENGINE - High Speed EV")
            print("-> Motor Main, Engine Assist")

# Test Toyota Scenarios
hybrid_control(30, 40)   # Low battery - Engine charges
hybrid_control(50, 90)   # Normal battery, high power - Both!
hybrid_control(75, 30)   # High battery, low power - EV Mode
hybrid_control(75, 85)   # High battery, high power - EV+Engine

print("\nP4 Complete - Toyota Power Split Done! 🔥")# TOYOTA HYBRID P4 - ENGINE + MOTOR COMBINE
# Ebenezer - Ghana to Japan
# MEXT Project

print("=== TOYOTA HYBRID P4 - ENGINE + MOTOR COMBINE ===")

# Settings
LOW_SOC = 35
HIGH_SOC = 70
POWER_HIGH = 80  # High power demand

def hybrid_control(soc, power_demand):
    print(f"\n--- SOC: {soc}% | Power Demand: {power_demand}% ---")
    
    if soc < LOW_SOC:
        print("MODE: ENGINE ONLY - Battery LOW!")
        print("-> Engine ON, Charging Battery + Driving Wheels")
        print("-> Motor OFF - Protect Battery")
        
    elif soc >= LOW_SOC and soc <= HIGH_SOC:
        if power_demand > POWER_HIGH:
            print("MODE: HYBRID POWER - Engine + Motor!")
            print("-> Engine ON + Motor ON = Full Power!")
            print("-> For Acceleration / Hill Climb")
        else:
            print("MODE: NORMAL HYBRID - Efficient Drive")
            print("-> Engine ON, Motor Assist")
            
    elif soc > HIGH_SOC:
        if power_demand < 50:
            print("MODE: EV MODE - Electric Only!")
            print("-> Engine OFF, Motor ON - Silent & Clean!")
            print("-> Battery 70% -> 75% with Regen")
        else:
            print("MODE: EV + ENGINE - High Speed EV")
            print("-> Motor Main, Engine Assist")

# Test Toyota Scenarios
hybrid_control(30, 40)   # Low battery - Engine charges
hybrid_control(50, 90)   # Normal battery, high power - Both!
hybrid_control(75, 30)   # High battery, low power - EV Mode
hybrid_control(75, 85)   # High battery, high power - EV+Engine

print("\nP4 Complete - Toyota Power Split Done! 🔥")
