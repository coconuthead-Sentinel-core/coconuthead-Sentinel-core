"""
Quantum Nexus Forge API - REST API Implementation
Flask-based API server with comprehensive endpoints and hooks
"""

from flask import Flask, request, jsonify
from flask_cors import CORS
import datetime
from typing import Dict, Any, List
from quantum_nexus_forge import QuantumNexusForge
import json

# Initialize Flask application
app = Flask(__name__)
CORS(app)  # Enable CORS for cross-origin requests

# Initialize the Quantum Nexus Forge instance
nexus = QuantumNexusForge()

# API request history for monitoring
request_history = []
MAX_HISTORY = 100


# Middleware for request logging
@app.before_request
def log_request():
    """Log all incoming requests"""
    request_data = {
        "timestamp": datetime.datetime.now().isoformat(),
        "method": request.method,
        "path": request.path,
        "remote_addr": request.remote_addr,
        "user_agent": request.headers.get('User-Agent', 'Unknown')
    }
    request_history.append(request_data)
    if len(request_history) > MAX_HISTORY:
        request_history.pop(0)


@app.after_request
def add_headers(response):
    """Add custom headers to all responses"""
    response.headers['X-Quantum-Nexus-Version'] = '6.0'
    response.headers['X-Shannon-Kelly-Protocols'] = 'Active'
    return response


# Core API Endpoints

@app.route('/')
def index():
    """Root endpoint with API information"""
    return jsonify({
        "name": "Quantum Nexus Forge API",
        "version": "6.0",
        "author": "Shannon Bryan Kelly (Coconut Head)",
        "status": "operational",
        "timestamp": datetime.datetime.now().isoformat(),
        "endpoints": {
            "health": "/api/health",
            "status": "/api/status",
            "process": "/api/process",
            "filing": "/api/filing",
            "bridges": "/api/bridges",
            "triadic": "/api/triadic",
            "geometry": "/api/geometry",
            "history": "/api/history"
        }
    })


@app.route('/api/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({
        "status": "healthy",
        "timestamp": datetime.datetime.now().isoformat(),
        "system_resonance": nexus.system_resonance,
        "active_bridges": len(nexus.hyphenator_registry),
        "triadic_processors": len(nexus.triadic_processors)
    })


@app.route('/api/status', methods=['GET'])
def get_status():
    """Get comprehensive system status"""
    status = nexus.get_system_status()
    return jsonify({
        "success": True,
        "data": status,
        "timestamp": datetime.datetime.now().isoformat()
    })


@app.route('/api/process', methods=['POST'])
def process_input():
    """Process user input through the cognitive architecture"""
    try:
        data = request.get_json()
        
        if not data or 'input' not in data:
            return jsonify({
                "success": False,
                "error": "Missing 'input' field in request body"
            }), 400
        
        user_input = data['input']
        context = data.get('context', None)
        
        # Process through Quantum Nexus Forge
        result = nexus.process_input(user_input, context)
        
        return jsonify({
            "success": True,
            "data": result,
            "timestamp": datetime.datetime.now().isoformat()
        })
    
    except Exception as e:
        return jsonify({
            "success": False,
            "error": str(e),
            "timestamp": datetime.datetime.now().isoformat()
        }), 500


@app.route('/api/filing', methods=['GET'])
def get_filing_system():
    """Get A1 filing system status"""
    return jsonify({
        "success": True,
        "data": {
            "green_zone": len(nexus.filing_system.get('green_zone', [])),
            "yellow_zone": len(nexus.filing_system.get('yellow_zone', [])),
            "red_zone": len(nexus.filing_system.get('red_zone', [])),
            "total_items": sum([
                len(nexus.filing_system.get('green_zone', [])),
                len(nexus.filing_system.get('yellow_zone', [])),
                len(nexus.filing_system.get('red_zone', []))
            ])
        },
        "timestamp": datetime.datetime.now().isoformat()
    })


@app.route('/api/bridges', methods=['GET'])
def get_bridges():
    """Get hyphenator bridge information"""
    bridges_data = {}
    for bridge_id, bridge in nexus.hyphenator_registry.items():
        bridges_data[bridge_id] = {
            "type": bridge.bridge_type.value,
            "source": bridge.source_component,
            "target": bridge.target_component,
            "function": bridge.bridge_function,
            "execution_count": bridge.execution_count,
            "success_rate": bridge.success_rate,
            "created_at": bridge.created_at
        }
    
    return jsonify({
        "success": True,
        "data": bridges_data,
        "total_bridges": len(bridges_data),
        "timestamp": datetime.datetime.now().isoformat()
    })


@app.route('/api/bridges/<bridge_id>/execute', methods=['POST'])
def execute_bridge(bridge_id):
    """Execute a specific hyphenator bridge"""
    try:
        if bridge_id not in nexus.hyphenator_registry:
            return jsonify({
                "success": False,
                "error": f"Bridge '{bridge_id}' not found"
            }), 404
        
        data = request.get_json()
        input_data = data.get('data', '')
        
        bridge = nexus.hyphenator_registry[bridge_id]
        result = bridge.execute_bridge(input_data)
        
        return jsonify({
            "success": True,
            "data": result,
            "timestamp": datetime.datetime.now().isoformat()
        })
    
    except Exception as e:
        return jsonify({
            "success": False,
            "error": str(e)
        }), 500


@app.route('/api/triadic', methods=['GET'])
def get_triadic_processors():
    """Get triadic processor information"""
    processors_data = {}
    for proc_id, processor in nexus.triadic_processors.items():
        processors_data[proc_id] = {
            "threshold": processor.consensus_threshold,
            "elements_count": len(processor.triadic_elements),
            "elements": [
                {
                    "icon": elem.icon,
                    "function": elem.function,
                    "description": elem.description,
                    "consensus_score": elem.consensus_score,
                    "active": elem.active
                } for elem in processor.triadic_elements
            ]
        }
    
    return jsonify({
        "success": True,
        "data": processors_data,
        "total_processors": len(processors_data),
        "timestamp": datetime.datetime.now().isoformat()
    })


@app.route('/api/triadic/<processor_id>/process', methods=['POST'])
def process_triadic(processor_id):
    """Process data through a specific triadic processor"""
    try:
        if processor_id not in nexus.triadic_processors:
            return jsonify({
                "success": False,
                "error": f"Processor '{processor_id}' not found"
            }), 404
        
        data = request.get_json()
        input_data = data.get('data', '')
        
        processor = nexus.triadic_processors[processor_id]
        result = processor.process_consensus(input_data)
        
        return jsonify({
            "success": True,
            "data": result,
            "timestamp": datetime.datetime.now().isoformat()
        })
    
    except Exception as e:
        return jsonify({
            "success": False,
            "error": str(e)
        }), 500


@app.route('/api/geometry', methods=['GET'])
def get_geometry():
    """Get sacred geometry primitive information"""
    geometry_data = {}
    for prim_name, primitive in nexus.geometric_primitives.items():
        geometry_data[prim_name] = {
            "vertex_count": primitive.vertex_count,
            "golden_ratio": primitive.golden_ratio,
            "sacred_frequencies": primitive.sacred_frequencies,
            "resonance_pattern_length": len(primitive.resonance_pattern)
        }
    
    return jsonify({
        "success": True,
        "data": geometry_data,
        "total_primitives": len(geometry_data),
        "timestamp": datetime.datetime.now().isoformat()
    })


@app.route('/api/geometry/<primitive_name>/harmony', methods=['POST'])
def calculate_harmony(primitive_name):
    """Calculate harmony for a specific geometric primitive"""
    try:
        if primitive_name not in nexus.geometric_primitives:
            return jsonify({
                "success": False,
                "error": f"Primitive '{primitive_name}' not found"
            }), 404
        
        data = request.get_json()
        entropy = data.get('entropy', 0.5)
        
        if not 0 <= entropy <= 1:
            return jsonify({
                "success": False,
                "error": "Entropy must be between 0 and 1"
            }), 400
        
        primitive = nexus.geometric_primitives[primitive_name]
        harmony = primitive.calculate_harmony(entropy)
        
        return jsonify({
            "success": True,
            "data": {
                "primitive": primitive_name,
                "input_entropy": entropy,
                "harmony_score": round(harmony, 3)
            },
            "timestamp": datetime.datetime.now().isoformat()
        })
    
    except Exception as e:
        return jsonify({
            "success": False,
            "error": str(e)
        }), 500


@app.route('/api/history', methods=['GET'])
def get_request_history():
    """Get API request history"""
    limit = request.args.get('limit', 20, type=int)
    limit = min(limit, MAX_HISTORY)
    
    return jsonify({
        "success": True,
        "data": request_history[-limit:],
        "total_requests": len(request_history),
        "timestamp": datetime.datetime.now().isoformat()
    })


# Webhook/Hook Endpoints

@app.route('/api/hooks/process', methods=['POST'])
def hook_process():
    """Webhook endpoint for external systems to process data"""
    try:
        data = request.get_json()
        
        # Validate webhook payload
        if not data or 'input' not in data:
            return jsonify({
                "success": False,
                "error": "Invalid webhook payload"
            }), 400
        
        # Process the input
        result = nexus.process_input(data['input'], data.get('context'))
        
        # Return webhook-friendly response
        return jsonify({
            "success": True,
            "webhook_id": data.get('webhook_id', 'unknown'),
            "response": result['response'],
            "intent": result['intent'],
            "concepts": result['concepts'],
            "processing_time_ms": result['processing_time_ms'],
            "timestamp": datetime.datetime.now().isoformat()
        })
    
    except Exception as e:
        return jsonify({
            "success": False,
            "error": str(e)
        }), 500


@app.route('/api/hooks/status', methods=['GET', 'POST'])
def hook_status():
    """Webhook endpoint for status checks"""
    return jsonify({
        "success": True,
        "status": "operational",
        "system_resonance": nexus.system_resonance,
        "timestamp": datetime.datetime.now().isoformat()
    })


# Error handlers

@app.errorhandler(404)
def not_found(error):
    return jsonify({
        "success": False,
        "error": "Endpoint not found",
        "timestamp": datetime.datetime.now().isoformat()
    }), 404


@app.errorhandler(500)
def internal_error(error):
    return jsonify({
        "success": False,
        "error": "Internal server error",
        "timestamp": datetime.datetime.now().isoformat()
    }), 500


# Run the application
if __name__ == '__main__':
    print("🚀 Starting Quantum Nexus Forge API Server")
    print("=" * 60)
    print("🟢 Shannon Bryan Kelly Protocols: ACTIVATED")
    print("🟢 Flask API Server: INITIALIZING")
    print("🟢 CORS: ENABLED")
    print("🟢 Endpoints: CONFIGURED")
    print("🟢 Webhooks: ACTIVE")
    print("=" * 60)
    print("\n📡 API Server running on http://127.0.0.1:5000")
    print("📚 API Documentation available at http://127.0.0.1:5000/")
    print("\n🔗 Available Endpoints:")
    print("  GET  /                      - API Information")
    print("  GET  /api/health            - Health Check")
    print("  GET  /api/status            - System Status")
    print("  POST /api/process           - Process Input")
    print("  GET  /api/filing            - Filing System")
    print("  GET  /api/bridges           - Hyphenator Bridges")
    print("  GET  /api/triadic           - Triadic Processors")
    print("  GET  /api/geometry          - Sacred Geometry")
    print("  GET  /api/history           - Request History")
    print("  POST /api/hooks/process     - Process Webhook")
    print("  GET  /api/hooks/status      - Status Webhook")
    print("\n" + "=" * 60)
    
    app.run(debug=True, host='0.0.0.0', port=5000)
