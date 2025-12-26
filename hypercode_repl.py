#!/usr/bin/env python3
"""
🧠 HyperCode REPL (Read-Eval-Print-Loop)
Interactive development environment for neurodivergent minds
<100ms feedback loops for ADHD brains
"""

import sys
import time
sys.path.insert(0, '.')

from hypercode_interpreter import tokenize, parse, execute

class HyperCodeREPL:
    def __init__(self):
        self.variables = {}
        self.functions = {}
        self.history = []
        self.start_time = time.time()
    
    def format_time(self):
        """Get current time for REPL"""
        elapsed = time.time() - self.start_time
        return elapsed
    
    def print_welcome(self):
        """Print welcome message"""
        print("\n" + "="*60)
        print("🧠 HyperCode REPL v0.9-beta")
        print("="*60)
        print("✨ Neurodivergent-first interactive programming")
        print()
        print("Commands:")
        print("  help      → Show all commands")
        print("  vars      → List all variables")
        print("  funcs     → List all functions")
        print("  clear     → Clear all variables")
        print("  history   → Show command history")
        print("  exit      → Quit REPL")
        print()
        print("Start typing HyperCode:")
        print("="*60 + "\n")
    
    def execute_code(self, code):
        """Execute HyperCode with error handling"""
        try:
            # Add semicolon if missing
            if not code.strip().endswith(';'):
                code = code.strip() + ';'
            
            # Tokenize
            tokens = tokenize(code)
            
            # Parse
            ast = parse(tokens)
            
            # Execute
            result = execute(ast, self.variables)
            
            # Store in history
            self.history.append(code)
            
            # Return result
            return result, None
        
        except SyntaxError as e:
            return None, f"❌ Syntax Error: {str(e)}\n   Tip: Check your brackets, quotes, and semicolons"
        except NameError as e:
            return None, f"❌ Name Error: {str(e)}\n   Tip: Variable not defined. Use 'vars' to see all variables"
        except TypeError as e:
            return None, f"❌ Type Error: {str(e)}\n   Tip: Wrong type for this operation"
        except Exception as e:
            return None, f"❌ Error: {str(e)}"
    
    def cmd_help(self):
        """Show help"""
        print("""
╔════════════════════════════════════════════════════════════╗
║                    HYPERCODE REPL HELP                    ║
╠════════════════════════════════════════════════════════════╣
║ BASIC COMMANDS                                             ║
║  print "text"      → Output text                           ║
║  let x = 5         → Create variable                       ║
║  print x           → Use variable                          ║
║  if x > 3 print x  → Conditional                           ║
║                                                            ║
║ REPL COMMANDS                                              ║
║  help              → Show this message                     ║
║  vars              → Show all variables                    ║
║  funcs             → Show all functions                    ║
║  clear             → Clear all variables                   ║
║  history           → Show recent commands                  ║
║  exit              → Quit REPL                             ║
║                                                            ║
║ EXAMPLES                                                   ║
║  print "Hello!";                                           ║
║  let name = "Alex";                                        ║
║  let age = 25;                                             ║
║  print name;                                               ║
║  print age;                                                ║
╚════════════════════════════════════════════════════════════╝
        """)
    
    def cmd_vars(self):
        """Show variables"""
        if not self.variables:
            print("📭 No variables defined yet")
            return
        
        print("\n📊 Variables:")
        for name, value in self.variables.items():
            if not name.startswith('_'):  # Skip internal vars
                print(f"  {name} = {value}")
        print()
    
    def cmd_history(self):
        """Show recent commands"""
        if not self.history:
            print("📭 No history yet")
            return
        
        print("\n📜 Recent commands:")
        for i, cmd in enumerate(self.history[-10:], 1):
            print(f"  {i}. {cmd}")
        print()
    
    def cmd_clear(self):
        """Clear all variables"""
        self.variables = {}
        print("✨ Cleared all variables")
    
    def run(self):
        """Main REPL loop"""
        self.print_welcome()
        
        while True:
            try:
                # Prompt (minimal for ADHD focus)
                line = input(">>> ").strip()
                
                # Skip empty lines
                if not line:
                    continue
                
                # Handle commands
                if line.lower() == 'exit':
                    print("\n👋 Goodbye! Keep coding. 💓\n")
                    break
                
                if line.lower() == 'help':
                    self.cmd_help()
                    continue
                
                if line.lower() == 'vars':
                    self.cmd_vars()
                    continue
                
                if line.lower() == 'history':
                    self.cmd_history()
                    continue
                
                if line.lower() == 'clear':
                    self.cmd_clear()
                    continue
                
                if line.lower() == 'funcs':
                    if self.functions:
                        print("\n🔧 Functions:")
                        for name in self.functions:
                            print(f"  - {name}")
                        print()
                    else:
                        print("📭 No functions defined yet\n")
                    continue
                
                # Execute code
                result, error = self.execute_code(line)
                
                if error:
                    print(error)
                elif result is not None:
                    print(f"=> {result}")
            
            except KeyboardInterrupt:
                print("\n\n👋 Interrupted. Type 'exit' to quit.\n")
            except Exception as e:
                print(f"❌ REPL Error: {str(e)}")

if __name__ == '__main__':
    repl = HyperCodeREPL()
    repl.run()
