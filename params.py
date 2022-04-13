URL_COMMUN = ["https://www.amazon.fr/Victorinox-1-3703-Couteau-10-Rouge/product-reviews/B00004YVBA/ref=cm_cr_getr_d_paging_btm_next_","?ie=UTF8&reviewerType=all_reviews&pageNumber="]
AMAZON_URL = "https://www.amazon.fr/"

DRIVER_PATH = r"/home/chenow/Documents/JCS/formation_scraping/chromedriver_linux64/chromedriver"

MODE = "PROD"
MOT_A_DETECTER = {
"est robuste" :["très résistant", "plûtot résistant", "semble résistant", "très robuste", "plûtot robuste", "semble robuste", "très solide", "plutôt solide", "semble solide"],
"a cassé" : ["a cassé", "est cassé", "semble fragile", "pas solide", "peu solide", "pas l'air solide"],
"bon prix" :["pas cher", "pas chère", "bon prix", "bon rapport qualité prix", "bon rapport qualité-prix", "bon rapport qualité/prix", "bon rapport qualite prix"],
"est tranchante" : ["coupe bien", "bon tranchant", "lame tranchante", "est tranchante", "est tranchant"],
"jolie" : ["est jolie", "très jolie", "plutôt jolie", "très beau", "beau couteau"],
"moche" : ["est moche", "pas beau", "plutôt moche"],
"maniable" : ["est pratique", "semble pratique", "plutôt pratique", "très pratique", "tres pratique", "plutot pratique"],
}



# https://www.amazon.fr/HONZIN-Couteau-Poche-Multifonctions-Suisse/product-reviews/B07F5ZN6MR/ref=cm_cr_arp_d_paging_btm_next_1?ie=UTF8&reviewerType=all_reviews&pageNumber=1

# https://www.amazon.fr/Victorinox-1-3703-Couteau-10-Rouge/product-reviews/B00004YVBA/ref=cm_cr_getr_d_paging_btm_next_3?ie=UTF8&reviewerType=all_reviews&pageNumber=3