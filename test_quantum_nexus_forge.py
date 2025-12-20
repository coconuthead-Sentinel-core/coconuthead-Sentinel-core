"""
Unit tests for Quantum Nexus Forge v6.0
Tests the core functionality of the enhanced cognitive architecture
"""

import unittest
from quantum_nexus_forge import (
    EnhancedQuantumNexusForge,
    HyphenatorType,
    HyphenatorNode,
    TriadicProcessor,
    TriadicElement,
    GeometricPrimitive
)


class TestTriadicElement(unittest.TestCase):
    """Test the TriadicElement class"""
    
    def test_triadic_element_creation(self):
        """Test creating a triadic element"""
        element = TriadicElement("🧠", "think()", "Cognitive processing")
        self.assertEqual(element.icon, "🧠")
        self.assertEqual(element.function, "think()")
        self.assertEqual(element.description, "Cognitive processing")
        self.assertEqual(element.consensus_score, 0.0)
        self.assertTrue(element.active)
    
    def test_triadic_element_to_tuple(self):
        """Test converting triadic element to tuple"""
        element = TriadicElement("📥", "input()", "Data reception")
        result = element.to_tuple()
        self.assertEqual(result, ("📥", "input()", "Data reception"))


class TestHyphenatorNode(unittest.TestCase):
    """Test the HyphenatorNode class"""
    
    def test_hyphenator_node_creation(self):
        """Test creating a hyphenator node"""
        bridge = HyphenatorNode(
            bridge_id="test-bridge",
            bridge_type=HyphenatorType.MEMORY_BRIDGE,
            source_component="Source",
            target_component="Target",
            bridge_function="MEMORY_BRIDGE-link()"
        )
        self.assertEqual(bridge.bridge_id, "test-bridge")
        self.assertEqual(bridge.bridge_type, HyphenatorType.MEMORY_BRIDGE)
        self.assertEqual(bridge.execution_count, 0)
        self.assertEqual(bridge.success_rate, 1.0)
    
    def test_hyphenator_bridge_execution(self):
        """Test executing a hyphenator bridge"""
        bridge = HyphenatorNode(
            bridge_id="test-bridge",
            bridge_type=HyphenatorType.COGNITIVE_BRIDGE,
            source_component="Input",
            target_component="Output",
            bridge_function="COGNITIVE_BRIDGE-synthesize()"
        )
        result = bridge.execute_bridge("test data")
        self.assertEqual(bridge.execution_count, 1)
        self.assertIn("bridge_id", result)
        self.assertIn("result", result)
        self.assertTrue(result["success"])


class TestTriadicProcessor(unittest.TestCase):
    """Test the TriadicProcessor class"""
    
    def test_triadic_processor_creation(self):
        """Test creating a triadic processor"""
        processor = TriadicProcessor("test_processor")
        self.assertEqual(processor.processor_id, "test_processor")
        self.assertEqual(len(processor.triadic_elements), 0)
        self.assertEqual(processor.consensus_threshold, 0.8)
    
    def test_adding_triadic_elements(self):
        """Test adding triadic elements"""
        processor = TriadicProcessor("test_processor")
        processor.add_triadic_element("🧠", "reason()", "Logical analysis")
        processor.add_triadic_element("💡", "synthesize()", "Creative combination")
        processor.add_triadic_element("⚖️", "evaluate()", "Quality assessment")
        self.assertEqual(len(processor.triadic_elements), 3)
    
    def test_consensus_processing(self):
        """Test triadic consensus processing"""
        processor = TriadicProcessor("test_processor")
        processor.add_triadic_element("📥", "input()", "Data reception")
        processor.add_triadic_element("🔍", "analyze()", "Pattern recognition")
        processor.add_triadic_element("🏷️", "categorize()", "Semantic tagging")
        
        result = processor.process_consensus("test input data")
        self.assertIn("processor_id", result)
        self.assertIn("consensus_achieved", result)
        self.assertIn("consensus_score", result)
        self.assertIn("processed_elements", result)
        self.assertEqual(len(result["processed_elements"]), 3)


class TestGeometricPrimitive(unittest.TestCase):
    """Test the GeometricPrimitive class"""
    
    def test_geometric_primitive_creation(self):
        """Test creating a geometric primitive"""
        primitive = GeometricPrimitive("tetrahedron", 4)
        self.assertEqual(primitive.primitive_type, "tetrahedron")
        self.assertEqual(primitive.vertex_count, 4)
        self.assertEqual(len(primitive.resonance_pattern), 4)
        self.assertEqual(primitive.golden_ratio, 1.618033988749)
    
    def test_harmony_calculation(self):
        """Test calculating harmonic resonance"""
        primitive = GeometricPrimitive("cube", 8)
        harmony = primitive.calculate_harmony(0.5)
        self.assertIsInstance(harmony, float)
        self.assertGreaterEqual(harmony, 0.0)
        self.assertLessEqual(harmony, 1.0)


class TestEnhancedQuantumNexusForge(unittest.TestCase):
    """Test the main EnhancedQuantumNexusForge class"""
    
    def setUp(self):
        """Set up test fixture"""
        self.nexus = EnhancedQuantumNexusForge()
    
    def test_system_initialization(self):
        """Test that the system initializes correctly"""
        self.assertIsNotNone(self.nexus.filing_system)
        self.assertIsNotNone(self.nexus.symbolic_processor)
        self.assertIsNotNone(self.nexus.hyphenator_registry)
        self.assertIsNotNone(self.nexus.triadic_processors)
        self.assertIsNotNone(self.nexus.geometric_primitives)
        
        # Check that all components are initialized
        self.assertEqual(len(self.nexus.hyphenator_registry), 5)
        self.assertEqual(len(self.nexus.triadic_processors), 3)
        self.assertEqual(len(self.nexus.geometric_primitives), 7)
    
    def test_hyphenator_bridges_initialized(self):
        """Test that hyphenator bridges are properly initialized"""
        expected_bridges = [
            "memory-cognitive",
            "cognitive-output",
            "process-validation",
            "reflection-integration",
            "output-harmonization"
        ]
        for bridge_id in expected_bridges:
            self.assertIn(bridge_id, self.nexus.hyphenator_registry)
    
    def test_triadic_processors_initialized(self):
        """Test that triadic processors are properly initialized"""
        expected_processors = [
            "data_reception",
            "cognitive_processing",
            "output_generation"
        ]
        for processor_id in expected_processors:
            self.assertIn(processor_id, self.nexus.triadic_processors)
            processor = self.nexus.triadic_processors[processor_id]
            self.assertEqual(len(processor.triadic_elements), 3)
    
    def test_geometric_primitives_initialized(self):
        """Test that geometric primitives are properly initialized"""
        expected_primitives = [
            "tetrahedron",
            "cube",
            "octahedron",
            "dodecahedron",
            "icosahedron",
            "metatron_cube",
            "flower_of_life"
        ]
        for primitive_name in expected_primitives:
            self.assertIn(primitive_name, self.nexus.geometric_primitives)
    
    def test_process_enhanced_input(self):
        """Test processing enhanced input"""
        result = self.nexus.process_enhanced_input("Hello, test the system")
        
        # Check that all expected keys are in the result
        expected_keys = [
            "timestamp",
            "processing_time_ms",
            "system_resonance",
            "phases",
            "bridge_executions",
            "sacred_geometry_harmony",
            "enhanced_response",
            "hyphenator_status",
            "triadic_consensus"
        ]
        for key in expected_keys:
            self.assertIn(key, result)
        
        # Check that phases contain expected sub-results
        self.assertIn("data_reception", result["phases"])
        self.assertIn("cognitive_processing", result["phases"])
        self.assertIn("output_generation", result["phases"])
        
        # Check that system resonance is within valid range
        self.assertGreaterEqual(result["system_resonance"], 0.0)
        self.assertLessEqual(result["system_resonance"], 1.0)
        
        # Check that processing time is non-negative
        self.assertGreaterEqual(result["processing_time_ms"], 0.0)
    
    def test_get_system_status(self):
        """Test getting system status"""
        status = self.nexus.get_system_status()
        
        # Check that all expected keys are present
        expected_keys = [
            "version",
            "timestamp",
            "system_resonance",
            "active_bridges",
            "triadic_processors",
            "geometric_primitives",
            "bridge_executions_total",
            "consensus_metrics",
            "sacred_geometry_status"
        ]
        for key in expected_keys:
            self.assertIn(key, status)
        
        # Check specific values
        self.assertEqual(status["version"], "6.0 - Shannon Bryan Kelly Enhanced")
        self.assertEqual(status["active_bridges"], 5)
        self.assertEqual(status["triadic_processors"], 3)
        self.assertEqual(status["geometric_primitives"], 7)
    
    def test_multiple_inputs(self):
        """Test processing multiple inputs sequentially"""
        inputs = [
            "Hello, system!",
            "Show me the status",
            "How does this work?"
        ]
        
        for test_input in inputs:
            result = self.nexus.process_enhanced_input(test_input)
            self.assertIsNotNone(result)
            self.assertIn("enhanced_response", result)
            self.assertIsInstance(result["enhanced_response"], str)
    
    def test_bridge_execution_logging(self):
        """Test that bridge executions are logged"""
        initial_log_size = len(self.nexus.bridge_execution_log)
        self.nexus.process_enhanced_input("Test logging")
        final_log_size = len(self.nexus.bridge_execution_log)
        self.assertGreater(final_log_size, initial_log_size)


def run_tests():
    """Run all tests and print results"""
    # Create test suite
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    
    # Add all test cases
    suite.addTests(loader.loadTestsFromTestCase(TestTriadicElement))
    suite.addTests(loader.loadTestsFromTestCase(TestHyphenatorNode))
    suite.addTests(loader.loadTestsFromTestCase(TestTriadicProcessor))
    suite.addTests(loader.loadTestsFromTestCase(TestGeometricPrimitive))
    suite.addTests(loader.loadTestsFromTestCase(TestEnhancedQuantumNexusForge))
    
    # Run tests with verbose output
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    # Print summary
    print("\n" + "=" * 60)
    print("TEST SUMMARY")
    print("=" * 60)
    print(f"Tests run: {result.testsRun}")
    print(f"Successes: {result.testsRun - len(result.failures) - len(result.errors)}")
    print(f"Failures: {len(result.failures)}")
    print(f"Errors: {len(result.errors)}")
    print("=" * 60)
    
    return result.wasSuccessful()


if __name__ == "__main__":
    success = run_tests()
    exit(0 if success else 1)
