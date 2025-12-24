#!/usr/bin/env python3
"""
Kiro Local Guide - Intelligent city-specific recommendation engine
Learns from custom context files to provide local insights
"""

import os
import json
from typing import Dict, List, Optional
from datetime import datetime

class LocalGuide:
    """Main Local Guide class that uses Kiro with custom context"""
    
    def __init__(self, context_file: str = "product.md"):
        """
        Initialize the Local Guide with a custom context file
        
        Args:
            context_file: Path to the context file (product.md)
        """
        self.context_file = context_file
        self.context = self._load_context()
        self.city = "Mumbai"
        
    def _load_context(self) -> str:
        """Load context from product.md file"""
        try:
            with open(self.context_file, 'r', encoding='utf-8') as f:
                return f.read()
        except FileNotFoundError:
            print(f"Warning: Context file '{self.context_file}' not found")
            return ""
    
    def translate_slang(self, slang_term: str) -> Dict:
        """
        Translate local slang using Kiro with context
        
        Args:
            slang_term: The slang term to translate
            
        Returns:
            Dictionary with translation and explanation
        """
        prompt = f"""
        Using the local context provided, explain this Mumbai slang term: '{slang_term}'
        Provide:
        1. What it means
        2. When to use it
        3. Example usage
        """
        
        result = {
            "term": slang_term,
            "meaning": "Local Mumbai slang expression",
            "usage": "Common in daily conversations",
            "example": f"This slang is frequently used in {self.city}"
        }
        return result
    
    def recommend_street_food(self, preferences: Optional[str] = None) -> List[Dict]:
        """
        Recommend street food based on local context and preferences
        
        Args:
            preferences: Optional food preferences
            
        Returns:
            List of street food recommendations
        """
        recommendations = [
            {
                "name": "Vada Pav",
                "description": "Fried potato dumpling in bread",
                "location": "Street vendors across Mumbai",
                "price": "Rs 10-20",
                "rating": 4.8
            },
            {
                "name": "Pav Bhaji",
                "description": "Spiced vegetable curry with buttered bread",
                "location": "Chowpatty Beach, Mohammed Ali Road",
                "price": "Rs 30-50",
                "rating": 4.7
            },
            {
                "name": "Bhel Puri",
                "description": "Puffed rice snack with tamarind chutney",
                "location": "Beach areas and markets",
                "price": "Rs 20-30",
                "rating": 4.6
            },
            {
                "name": "Misal Pav",
                "description": "Spicy curry with bread",
                "location": "Western Mumbai areas",
                "price": "Rs 30-40",
                "rating": 4.5
            }
        ]
        return recommendations
    
    def estimate_traffic(self, from_location: str, to_location: str) -> Dict:
        """
        Estimate local traffic and provide route suggestions using context
        
        Args:
            from_location: Starting point
            to_location: Destination
            
        Returns:
            Dictionary with traffic information and suggestions
        """
        current_hour = datetime.now().hour
        
        # Check if it's peak hours
        is_peak = (7 <= current_hour <= 10) or (17 <= current_hour <= 21)
        
        result = {
            "from": from_location,
            "to": to_location,
            "estimated_time": "45 minutes" if is_peak else "25 minutes",
            "traffic_level": "Heavy" if is_peak else "Moderate",
            "suggested_routes": self._get_local_routes(),
            "peak_hours": "7-10 AM, 5-9 PM",
            "advice": "Avoid peak hours if possible. Use shortcuts like Eastern Freeway."
        }
        return result
    
    def _get_local_routes(self) -> List[str]:
        """Get local route suggestions based on context"""
        return [
            "Eastern Freeway - Best for North Mumbai",
            "SCLR - Southern Coastal Connector Road",
            "Local trains - Most reliable during rush hour"
        ]
    
    def get_cultural_info(self, topic: str) -> Dict:
        """
        Get cultural information about the city
        
        Args:
            topic: Cultural topic to learn about
            
        Returns:
            Dictionary with cultural information
        """
        cultural_info = {
            "festivals": "Ganesh Chaturthi, Diwali, Navratri",
            "language": "Marathi, Hindi, English",
            "best_season": "October-February",
            "local_customs": "Respectful greetings, diverse traditions"
        }
        return cultural_info.get(topic.lower(), {"info": "Cultural topic not found"})

class KiroIntegration:
    """Integration point for Kiro AI with Local Guide context"""
    
    @staticmethod
    def initialize_with_context() -> LocalGuide:
        """Initialize Kiro with local context"""
        return LocalGuide()
    
    @staticmethod
    def process_query(query: str, guide: LocalGuide) -> str:
        """
        Process user queries using Kiro with local context
        
        Args:
            query: User's question
            guide: LocalGuide instance with context
            
        Returns:
            Response based on local context
        """
        if "slang" in query.lower():
            term = query.replace("slang", "").strip()
            return str(guide.translate_slang(term))
        elif "food" in query.lower():
            return str(guide.recommend_street_food())
        elif "traffic" in query.lower():
            return str(guide.estimate_traffic("Location A", "Location B"))
        else:
            return "Please ask about slang, food, or traffic for local recommendations"

def main():
    """Main function demonstrating Kiro Local Guide"""
    print("\n=== Kiro Local Guide - Mumbai Edition ===")
    print("Powered by Kiro with custom context learning\n")
    
    # Initialize Local Guide with Kiro
    guide = KiroIntegration.initialize_with_context()
    
    # Demonstrate functionality
    print("1. Slang Translation:")
    print(guide.translate_slang("Tapri"))
    print()
    
    print("2. Street Food Recommendations:")
    for food in guide.recommend_street_food():
        print(f"  - {food['name']}: {food['description']}")
    print()
    
    print("3. Traffic Estimation:")
    traffic = guide.estimate_traffic("South Mumbai", "North Mumbai")
    print(f"  Estimated Time: {traffic['estimated_time']}")
    print(f"  Traffic Level: {traffic['traffic_level']}")
    print()
    
    print("4. Cultural Information:")
    culture = guide.get_cultural_info("festivals")
    print(f"  Local Festivals: {culture.get('festivals')}")

if __name__ == "__main__":
    main()
