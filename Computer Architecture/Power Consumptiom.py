def total_power_consumption(voltage, frequency, capacitive_load, leakage_current, alpha=1.0, name=None, description=None):
    """
    Calculate the total power consumption of a system based on dynamic and static power components.

    Parameters:
    - voltage (float): Operating voltage in Volts.
    - frequency (float): Clock frequency in Hz.
    - capacitive_load (float): Capacitive load in Farads.
    - static_power (float): Static power consumption in Watts.
    - alpha (float, optional): Activity factor, defaults to 1.0 if not specified.
    - name (str, optional): Name of the system or component.
    - description (str, optional): Description of the system or component.

    Returns:
    - float: Total power consumption in Watts.
    """
    # Calculate dynamic power
    dynamic_power = alpha * capacitive_load * (voltage ** 2) * frequency
    static_power = leakage_current * voltage

    # Calculate total power
    total_power = dynamic_power + static_power

    # Optionally print the name and description if they are provided
    if name or description:
        print(f"Calculating power for: {name if name else 'Unnamed System'}")
        if description:
            print(f"Description: {description}")

    return total_power

def cal_load_capacitance(dynamic_power, voltage, frequency, alpha=1.0):
    load_capacitance = dynamic_power / (alpha * frequency * voltage ** 2)
    return load_capacitance

if __name__ == "__main__":

    # Example usage with name and description
    '''
    The Pentium 4 Prescott, released in 2004, has a clock rate of 3.6 GHz and voltage of 1.6 V. 
    Assume that, on average, it consumed 10 W of static power and 90 W of dynamic power.
    '''

    # Creating a list of dictionaries with the given information
    CPUs = [
        {
            "name": "Pentium 4 Prescott",
            "description": "The Pentium 4 Prescott, released in 2004.",
            "voltage": 1.6,  # Volts
            "frequency": 3.6 * 10 ** 9,  # Hz
            "dynamic_power": 90  # Watts
        },
        {
            "name": "Core i7-3770 (Ivy Bridge)",
            "description": "The Core i7-3770 (Ivy Bridge), released in 2012.",
            "voltage": 1.2,  # Volts
            "frequency": 3.4 * 10 ** 9,  # Hz
            "dynamic_power": 47  # Watts
        },
        {
            "name": "Core i3-530",
            "description": "The Core i3-530, released in 2010.",
            "voltage": 1.4,  # Volts
            "frequency": 2.93 * 10 ** 9,  # Hz
            "dynamic_power": 63  # Watts
        },
        {
            "name": "Core i5-5675R (Broadwell)",
            "description": "The Core i5-5675R (Broadwell), released in 2015.",
            "voltage": 1.0,  # Volts
            "frequency": 3.4 * 10 ** 9,  # Hz
            "dynamic_power": 45  # Watts
        },
        {
            "name": "Core i7-1065G7 (Ice Lake)",
            "description": "The Core i7-1065G7 (Ice Lake), released in 2019.",
            "voltage": 0.8,  # Volts
            "frequency": 1.3 * 10 ** 9,  # Hz
            "dynamic_power": 20  # Watts
        },
    ]
    for cpu in CPUs:
        name = cpu['name']
        dynamic_power = cpu["dynamic_power"]
        voltage = cpu["voltage"]
        frequency = cpu["frequency"]
        capacitive_load = cal_load_capacitance(dynamic_power, voltage, frequency)  # Farads
        print(f"Capacitive load of {name}: {capacitive_load} F")



