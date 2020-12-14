import os
from api import api




if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    api.run(host='0.0.0.0', port=port)
