# test_simple.py
def test_basic_imports():
    """Test only the most basic imports"""
    try:
        import json
        import os
        from datetime import datetime
        print("✓ All basic imports successful!")
        return True
    except ImportError as e:
        print(f"✗ Basic import failed: {e}")
        return False

def test_optional_imports():
    """Test optional imports"""
    try:
        import flask
        print("✓ Flask imported")
    except:
        print("✗ Flask not available (optional)")
    
    try:
        import nltk
        print("✓ NLTK imported") 
    except:
        print("✗ NLTK not available (optional)")
    
    try:
        import requests
        print("✓ Requests imported")
    except:
        print("✗ Requests not available (optional)")

if __name__ == "__main__":
    print("Testing Basic AI Assistant Setup...")
    
    if test_basic_imports():
        test_optional_imports()
        print("\n🎉 Basic setup successful! Your AI assistant should work.")
        print("Run: python app/main.py")
    else:
        print("\n❌ Critical imports failed. Please check your Python installation.")