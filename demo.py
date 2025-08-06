from quantum_nexus_forge import QuantumNexusForge

# Initialize the system
nexus = QuantumNexusForge()

# Process user input
result = nexus.process_input("Hello! Tell me about cognitive architecture.")

# Access response
print(result['response'])
print(f"Intent: {result['intent']['type']}")
print(f"Concepts: {result['concepts']}")
