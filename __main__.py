import uvicorn
from src.config import *
from src.enrichment_api import enrichment_api



def main():
    uvicorn.run(enrichment_api, host=ENRICHMENT_HOST, port=int(ENRICHMENT_PORT))

if __name__ == "__main__":
    main()
   