"""
Test Suite for Quantum Nexus Forge
Comprehensive testing for all components
"""

import unittest
import json
from quantum_nexus_forge import QuantumNexusForge, HyphenatorType, TriadicElement, HyphenatorNode, TriadicProcessor, GeometricPrimitive


class TestQuantumNexusForge(unittest.TestCase):
    """Test the main QuantumNexusForge class"""
    
    def setUp(self):
        """Initialize test instance"""
        self.nexus = QuantumNexusForge()
    
    def test_initialization(self):
        """Test that the system initializes correctly"""
        self.assertIsNotNone(self.nexus)
        self.assertEqual(len(self.nexus.hyphenator_registry), 5)
        self.assertEqual(len(self.nexus.triadic_processors), 3)
        self.assertEqual(len(self.nexus.geometric_primitives), 7)
    
    def test_process_input_greeting(self):
        """Test processing a greeting"""
        result = self.nexus.process_input("Hello!")
        self.assertIsNotNone(result)
        self.assertIn('response', result)
        self.assertIn('intent', result)
        self.assertEqual(result['intent']['type'], 'greeting')
    
    def test_process_input_status(self):
        """Test processing a status query"""
        result = self.nexus.process_input("Show me the system status")
        self.assertIsNotNone(result)
        self.assertEqual(result['intent']['type'], 'status_query')
    
    def test_process_input_cognitive(self):
        """Test processing a cognitive architecture query"""
        result = self.nexus.process_input("Tell me about cognitive architecture")
        self.assertIsNotNone(result)
        self.assertIn('cognitive', result['concepts'])
        self.assertIn('architecture', result['concepts'])
    
    def test_system_resonance(self):
        """Test system resonance calculation"""
        result = self.nexus.process_input("Test input")
        self.assertIn('system_resonance', result)
        self.assertGreater(result['system_resonance'], 0)
        self.assertLessEqual(result['system_resonance'], 1)
    
    def test_processing_time(self):
        """Test that processing time is recorded"""
        result = self.nexus.process_input("Test input")
        self.assertIn('processing_time_ms', result)
        self.assertGreater(result['processing_time_ms'], 0)
    
    def test_get_system_status(self):
        """Test getting system status"""
        status = self.nexus.get_system_status()
        self.assertIsNotNone(status)
        self.assertIn('version', status)
        self.assertIn('active_bridges', status)
        self.assertIn('triadic_processors', status)


class TestHyphenatorBridges(unittest.TestCase):
    """Test hyphenator bridge functionality"""
    
    def setUp(self):
        """Initialize test instance"""
        self.nexus = QuantumNexusForge()
    
    def test_bridge_count(self):
        """Test that all bridges are initialized"""
        self.assertEqual(len(self.nexus.hyphenator_registry), 5)
    
    def test_bridge_execution(self):
        """Test executing a bridge"""
        bridge = self.nexus.hyphenator_registry['memory-cognitive']
        result = bridge.execute_bridge("Test data")
        self.assertIsNotNone(result)
        self.assertEqual(result['success'], True)
        self.assertEqual(bridge.execution_count, 1)
    
    def test_bridge_types(self):
        """Test that bridges have correct types"""
        bridge = self.nexus.hyphenator_registry['memory-cognitive']
        self.assertEqual(bridge.bridge_type, HyphenatorType.MEMORY_BRIDGE)


class TestTriadicProcessors(unittest.TestCase):
    """Test triadic processor functionality"""
    
    def setUp(self):
        """Initialize test instance"""
        self.nexus = QuantumNexusForge()
    
    def test_processor_count(self):
        """Test that all processors are initialized"""
        self.assertEqual(len(self.nexus.triadic_processors), 3)
    
    def test_data_reception_processor(self):
        """Test data reception processor"""
        processor = self.nexus.triadic_processors['data_reception']
        self.assertEqual(len(processor.triadic_elements), 3)
        result = processor.process_consensus("Test input")
        self.assertIn('consensus_score', result)
        self.assertIn('consensus_achieved', result)
    
    def test_cognitive_processor(self):
        """Test cognitive processing processor"""
        processor = self.nexus.triadic_processors['cognitive_processing']
        result = processor.process_consensus("Test cognitive input")
        self.assertIsNotNone(result)
        self.assertGreater(result['consensus_score'], 0)
    
    def test_output_processor(self):
        """Test output generation processor"""
        processor = self.nexus.triadic_processors['output_generation']
        result = processor.process_consensus("Test output")
        self.assertIsNotNone(result)


class TestGeometricPrimitives(unittest.TestCase):
    """Test sacred geometry primitive functionality"""
    
    def setUp(self):
        """Initialize test instance"""
        self.nexus = QuantumNexusForge()
    
    def test_primitive_count(self):
        """Test that all primitives are initialized"""
        self.assertEqual(len(self.nexus.geometric_primitives), 7)
    
    def test_tetrahedron(self):
        """Test tetrahedron primitive"""
        tetrahedron = self.nexus.geometric_primitives['tetrahedron']
        self.assertEqual(tetrahedron.vertex_count, 4)
        self.assertAlmostEqual(tetrahedron.golden_ratio, 1.618033988749)
    
    def test_harmony_calculation(self):
        """Test harmony calculation"""
        tetrahedron = self.nexus.geometric_primitives['tetrahedron']
        harmony = tetrahedron.calculate_harmony(0.5)
        self.assertGreater(harmony, 0)
        self.assertLessEqual(harmony, 1)
    
    def test_resonance_patterns(self):
        """Test resonance pattern generation"""
        for primitive in self.nexus.geometric_primitives.values():
            self.assertEqual(len(primitive.resonance_pattern), primitive.vertex_count)


class TestTriadicElement(unittest.TestCase):
    """Test triadic element functionality"""
    
    def test_element_creation(self):
        """Test creating a triadic element"""
        element = TriadicElement("🧠", "think()", "Cognitive processing")
        self.assertEqual(element.icon, "🧠")
        self.assertEqual(element.function, "think()")
        self.assertEqual(element.description, "Cognitive processing")
        self.assertTrue(element.active)
    
    def test_element_tuple(self):
        """Test element to tuple conversion"""
        element = TriadicElement("🧠", "think()", "Cognitive processing")
        result = element.to_tuple()
        self.assertEqual(result, ("🧠", "think()", "Cognitive processing"))


class TestIntentExtraction(unittest.TestCase):
    """Test intent extraction functionality"""
    
    def setUp(self):
        """Initialize test instance"""
        self.nexus = QuantumNexusForge()
    
    def test_greeting_intent(self):
        """Test greeting intent detection"""
        result = self.nexus.process_input("Hello there!")
        self.assertEqual(result['intent']['type'], 'greeting')
    
    def test_status_intent(self):
        """Test status query intent detection"""
        result = self.nexus.process_input("What's the system status?")
        self.assertEqual(result['intent']['type'], 'status_query')
    
    def test_information_intent(self):
        """Test information request intent detection"""
        result = self.nexus.process_input("Tell me about the cognitive architecture")
        self.assertEqual(result['intent']['type'], 'information_request')


class TestConceptExtraction(unittest.TestCase):
    """Test concept extraction functionality"""
    
    def setUp(self):
        """Initialize test instance"""
        self.nexus = QuantumNexusForge()
    
    def test_cognitive_concept(self):
        """Test cognitive concept extraction"""
        result = self.nexus.process_input("How does cognitive processing work?")
        self.assertIn('cognitive', result['concepts'])
    
    def test_architecture_concept(self):
        """Test architecture concept extraction"""
        result = self.nexus.process_input("Tell me about the system architecture")
        self.assertIn('architecture', result['concepts'])
    
    def test_multiple_concepts(self):
        """Test multiple concept extraction"""
        result = self.nexus.process_input("Explain the cognitive architecture and memory processing")
        self.assertTrue(len(result['concepts']) >= 2)


class TestFilingSystem(unittest.TestCase):
    """Test A1 filing system"""
    
    def setUp(self):
        """Initialize test instance"""
        self.nexus = QuantumNexusForge()
    
    def test_filing_system_initialization(self):
        """Test filing system is initialized"""
        self.assertIsNotNone(self.nexus.filing_system)
        self.assertIn('green_zone', self.nexus.filing_system)
        self.assertIn('yellow_zone', self.nexus.filing_system)
        self.assertIn('red_zone', self.nexus.filing_system)


def run_tests():
    """Run all tests"""
    # Create test suite
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    
    # Add all test classes
    suite.addTests(loader.loadTestsFromTestCase(TestQuantumNexusForge))
    suite.addTests(loader.loadTestsFromTestCase(TestHyphenatorBridges))
    suite.addTests(loader.loadTestsFromTestCase(TestTriadicProcessors))
    suite.addTests(loader.loadTestsFromTestCase(TestGeometricPrimitives))
    suite.addTests(loader.loadTestsFromTestCase(TestTriadicElement))
    suite.addTests(loader.loadTestsFromTestCase(TestIntentExtraction))
    suite.addTests(loader.loadTestsFromTestCase(TestConceptExtraction))
    suite.addTests(loader.loadTestsFromTestCase(TestFilingSystem))
    
    # Run tests
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    # Print summary
    print("\n" + "=" * 60)
    print(f"Tests run: {result.testsRun}")
    print(f"Successes: {result.testsRun - len(result.failures) - len(result.errors)}")
    print(f"Failures: {len(result.failures)}")
    print(f"Errors: {len(result.errors)}")
    print("=" * 60)
    
    return result.wasSuccessful()


if __name__ == '__main__':
    success = run_tests()
    exit(0 if success else 1)
