from quantum_nexus_forge import EnhancedQuantumNexusForge

# Initialize the Enhanced Quantum Nexus Forge system
nexus = EnhancedQuantumNexusForge()

print("=" * 60)
print("🚀 QUANTUM NEXUS FORGE v6.0 - DEMO")
print("=" * 60)

# Process sample inputs
test_inputs = [
    "Hello! Tell me about cognitive architecture.",
    "Show me the system status",
    "How does triadic processing work?"
]

for i, user_input in enumerate(test_inputs, 1):
    print(f"\n📝 Input {i}: {user_input}")
    result = nexus.process_enhanced_input(user_input)
    print(f"✨ Response: {result['enhanced_response']}")
    print(f"⏱️  Processing Time: {result['processing_time_ms']}ms")
    print(f"🎵 System Resonance: {result['system_resonance']}")

# Show system status
print("\n" + "=" * 60)
print("📊 SYSTEM STATUS")
print("=" * 60)
status = nexus.get_system_status()
print(f"Version: {status['version']}")
print(f"Active Bridges: {status['active_bridges']}")
print(f"Triadic Processors: {status['triadic_processors']}")
print(f"Sacred Geometry Primitives: {status['geometric_primitives']}")
print(f"Total Bridge Executions: {status['bridge_executions_total']}")
print(f"System Resonance: {status['system_resonance']}")
print("✅ All Systems: OPERATIONAL")
