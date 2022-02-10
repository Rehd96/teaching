class Utility:
    
    @staticmethod
    def is_integer(num): 
        try: 
            if (num - int(num)) == 0: 
                return True
            return False
        except ValueError: 
            return False
