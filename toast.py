

class colors:
    GREEN = '\033[1m\033[92m'
    YELLOW_BOLD = '\033[1m\033[93m'
    YELLOW = '\033[93m'
    CYAN = '\033[1m\033[96m'
    RED = '\033[1m\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'

def toast(suffix = '', message = '', type=''):
    
    # Show a toast message
    if type == 'info':
        print(suffix + colors.CYAN + 'ℹ️  Info ' + colors.END + message)
    elif type == 'warning':
        print(suffix + colors.YELLOW_BOLD + ' ⚠️ Warning ' + colors.END + message)
    elif type == 'success':
        print(suffix + colors.GREEN + ' ✓ Success ' + colors.END + message  ) #'✅ '  
    elif type == 'error':
        print(suffix + colors.RED + ' 🚫 Error ' + colors.END + message)
    else:
        print(f"{suffix} " + message)   