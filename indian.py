class Colors:
    RED = "\033[91m"
    GREEN = "\033[92m"
    BLUE = "\033[94m"
    YELLOW = "\033[93m"
    CYAN = "\033[96m"
    MAGENTA = "\033[95m"
    WHITE = "\033[97m"
    BOLD = "\033[1m"
    RESET = "\033[0m"


SIMPLE = "simple"
STANDARD = "standard"
DETAILED = "detailed"

current_measurement_mode = SIMPLE

NON_VEG_KEYWORDS = ["chicken", "mutton", "fish", "lamb", "meat", "prawn", "shrimp", "egg", "pork", "beef", "hilsa", "ilish", "keema"]
DAIRY_KEYWORDS = ["milk", "cream", "paneer", "yogurt", "ghee", "curd", "khoya", "mawa", "cheese", "butter", "malai", "dahi"]
	

def create_ingredient(name, simple, standard, detailed):
    return {
        "name": name,
        "simple": simple,
        "standard": standard,
        "detailed": detailed
    }

def butter_chicken():
    return {
        "name": "Butter Chicken",
        "category": "North India",
        "ingredients": [
            create_ingredient("Chicken", "1 lb", "500g", "One pound of boneless chicken thighs, cut into 2-inch pieces"),
            create_ingredient("Butter", "4 tbsp", "60g", "Four tablespoons of unsalted butter, divided"),
            create_ingredient("Tomato Puree", "1 cup", "250ml", "One cup of smooth tomato puree from ripe tomatoes"),
            create_ingredient("Heavy Cream", "1/2 cup", "120ml", "Half cup of fresh heavy cream"),
            create_ingredient("Yogurt", "1/2 cup", "125g", "Half cup of thick plain yogurt for marination"),
            create_ingredient("Ginger-Garlic Paste", "2 tbsp", "30g", "Two tablespoons of freshly ground ginger-garlic paste"),
            create_ingredient("Garam Masala", "1 tsp", "5g", "One teaspoon of aromatic garam masala"),
            create_ingredient("Red Chili Powder", "1 tsp", "5g", "One teaspoon of Kashmiri red chili powder for color"),
            create_ingredient("Kasuri Methi", "1 tbsp", "3g", "One tablespoon of dried fenugreek leaves, crushed"),
            create_ingredient("Salt", "to taste", "to taste", "Salt adjusted to personal preference"),
            create_ingredient("Oil", "2 tbsp", "30ml", "Two tablespoons of neutral cooking oil"),
        ],
        "steps": [
            "Marinate chicken pieces in yogurt, half the ginger-garlic paste, red chili powder, and salt for at least 2 hours or overnight in the refrigerator.",
            "Heat oil and 2 tablespoons of butter in a heavy-bottomed pan over medium-high heat.",
            "Add marinated chicken pieces and cook until they are golden brown on all sides, about 5-7 minutes. Remove and set aside.",
            "In the same pan, add remaining butter and ginger-garlic paste. Sauté until fragrant, about 1 minute.",
            "Pour in the tomato puree and cook on medium heat for 10-15 minutes until oil separates and the gravy thickens.",
            "Add garam masala and mix well. Return the chicken to the pan.",
            "Simmer for 10 minutes until chicken is fully cooked through.",
            "Reduce heat to low, add heavy cream and crushed kasuri methi. Stir gently.",
            "Let it simmer for another 5 minutes. Adjust salt and serve hot with naan or rice.",
        ],
    }


def dal_makhani():
    return {
        "name": "Dal Makhani",
        "category": "North India",
        "ingredients": [
            create_ingredient("Black Lentils (Urad Dal)", "1 cup", "200g", "One cup of whole black lentils, soaked overnight"),
            create_ingredient("Kidney Beans (Rajma)", "1/4 cup", "50g", "Quarter cup of red kidney beans, soaked overnight"),
            create_ingredient("Butter", "4 tbsp", "60g", "Four tablespoons of unsalted butter"),
            create_ingredient("Heavy Cream", "1/2 cup", "120ml", "Half cup of fresh heavy cream"),
            create_ingredient("Tomato Puree", "1 cup", "250ml", "One cup of smooth tomato puree"),
            create_ingredient("Onion", "1 large", "150g", "One large onion, finely chopped"),
            create_ingredient("Ginger-Garlic Paste", "2 tbsp", "30g", "Two tablespoons of fresh ginger-garlic paste"),
            create_ingredient("Red Chili Powder", "1 tsp", "5g", "One teaspoon of Kashmiri red chili powder"),
            create_ingredient("Garam Masala", "1 tsp", "5g", "One teaspoon of aromatic garam masala"),
            create_ingredient("Salt", "to taste", "to taste", "Salt adjusted to preference"),
        ],
        "steps": [
            "Pressure cook soaked black lentils and kidney beans with 4 cups water and salt for 20-25 minutes until very soft.",
            "Mash some of the lentils to create a creamy texture while keeping some whole.",
            "Heat butter in a heavy pan, add chopped onions and sauté until golden brown.",
            "Add ginger-garlic paste and cook for 2 minutes until fragrant.",
            "Add tomato puree and cook for 10 minutes until oil separates.",
            "Add red chili powder and garam masala, mix well.",
            "Add the cooked lentils and simmer on low heat for 30-45 minutes, stirring occasionally.",
            "Add cream and more butter, simmer for another 15 minutes.",
            "The longer you simmer, the better the flavor. Serve hot with rice or naan.",
        ],
    }
def rogan_josh():
    return {
        "name": "Rogan Josh",
        "category": "North India",
        "ingredients": [
            create_ingredient("Lamb", "1 lb", "500g", "One pound of bone-in lamb pieces from leg or shoulder"),
            create_ingredient("Yogurt", "1 cup", "250g", "One cup of thick plain yogurt, whisked smooth"),
            create_ingredient("Onions", "2 large", "300g", "Two large onions, thinly sliced"),
            create_ingredient("Kashmiri Chili Powder", "2 tbsp", "15g", "Two tablespoons of mild Kashmiri chili for vibrant color"),
            create_ingredient("Fennel Powder", "1 tsp", "5g", "One teaspoon of ground fennel seeds"),
            create_ingredient("Ginger Powder", "1 tsp", "5g", "One teaspoon of dry ginger powder (saunth)"),
            create_ingredient("Ghee", "4 tbsp", "60g", "Four tablespoons of pure ghee"),
            create_ingredient("Bay Leaves", "2", "2 pieces", "Two dried bay leaves"),
            create_ingredient("Cardamom", "4 pods", "4 pods", "Four green cardamom pods, lightly crushed"),
            create_ingredient("Salt", "to taste", "to taste", "Salt adjusted to preference"),
        ],
        "steps": [
            "Heat ghee in a heavy-bottomed pan and add bay leaves and cardamom pods.",
            "Add sliced onions and fry until deep golden brown, about 15 minutes.",
            "Add lamb pieces and brown on all sides for 10 minutes.",
            "Mix Kashmiri chili powder with 2 tablespoons water to make a paste, add to the pan.",
            "Stir well and cook for 5 minutes until oil separates.",
            "Add whisked yogurt one tablespoon at a time, stirring continuously to prevent curdling.",
            "Add fennel powder, ginger powder, and salt. Mix well.",
            "Add 1 cup water, cover and simmer on low heat for 1-1.5 hours until lamb is tender.",
            "The gravy should be thick and oil should float on top. Serve with steamed rice.",
        ],
    }


def chole_bhature():
    return {
        "name": "Chole Bhature",
        "category": "North India",
        "ingredients": [
            create_ingredient("Chickpeas", "2 cups", "400g", "Two cups of dried chickpeas, soaked overnight"),
            create_ingredient("Onions", "2 large", "300g", "Two large onions, finely chopped"),
            create_ingredient("Tomatoes", "3 medium", "300g", "Three medium ripe tomatoes, pureed"),
            create_ingredient("Tea Bags", "2", "2 pieces", "Two black tea bags for dark color"),
            create_ingredient("Chole Masala", "2 tbsp", "20g", "Two tablespoons of punjabi chole masala"),
            create_ingredient("All-Purpose Flour", "2 cups", "250g", "Two cups of all-purpose flour for bhature"),
            create_ingredient("Yogurt", "1/4 cup", "60g", "Quarter cup of yogurt for bhatura dough"),
            create_ingredient("Oil", "for frying", "for frying", "Sufficient oil for deep frying bhature"),
            create_ingredient("Ginger-Garlic Paste", "2 tbsp", "30g", "Two tablespoons of fresh ginger-garlic paste"),
            create_ingredient("Green Chilies", "2", "10g", "Two green chilies, slit"),
        ],
        "steps": [
            "Pressure cook soaked chickpeas with tea bags and salt until very soft, about 20 minutes.",
            "For bhatura: Mix flour, yogurt, salt, sugar, and water to make soft dough. Rest for 2 hours.",
            "Heat oil in a pan, add cumin seeds and let them splutter.",
            "Add onions and fry until golden brown.",
            "Add ginger-garlic paste and green chilies, cook for 2 minutes.",
            "Add tomato puree and cook until oil separates.",
            "Add chole masala, turmeric, and cooked chickpeas with some cooking liquid.",
            "Simmer for 20 minutes, mashing some chickpeas for thick gravy.",
            "For bhature: Roll dough into oval shapes and deep fry until puffed and golden.",
            "Serve hot chole with bhature, sliced onions, and green chutney.",
        ],
    }


def paneer_tikka():
    return {
        "name": "Paneer Tikka",
        "category": "North India",
        "ingredients": [
            create_ingredient("Paneer", "400g", "400g", "Four hundred grams of fresh cottage cheese, cut into cubes"),
            create_ingredient("Yogurt", "1 cup", "250g", "One cup of thick hung yogurt"),
            create_ingredient("Bell Peppers", "2", "200g", "Two bell peppers (mixed colors), cut into squares"),
            create_ingredient("Onion", "1 large", "150g", "One large onion, cut into squares"),
            create_ingredient("Tikka Masala", "2 tbsp", "20g", "Two tablespoons of tikka masala powder"),
            create_ingredient("Ginger-Garlic Paste", "1 tbsp", "15g", "One tablespoon of fresh ginger-garlic paste"),
            create_ingredient("Lemon Juice", "2 tbsp", "30ml", "Two tablespoons of fresh lemon juice"),
            create_ingredient("Oil", "3 tbsp", "45ml", "Three tablespoons of mustard oil or neutral oil"),
            create_ingredient("Kasuri Methi", "1 tsp", "2g", "One teaspoon of dried fenugreek leaves"),
            create_ingredient("Salt", "to taste", "to taste", "Salt adjusted to preference"),
        ],
        "steps": [
            "Whisk together yogurt, tikka masala, ginger-garlic paste, lemon juice, oil, kasuri methi, and salt.",
            "Add paneer cubes, bell peppers, and onion pieces to the marinade.",
            "Mix gently to coat everything evenly. Marinate for at least 1 hour.",
            "Thread marinated paneer and vegetables onto skewers alternately.",
            "Preheat oven to 220°C (425°F) or prepare a charcoal grill.",
            "Place skewers on a baking tray lined with foil, brush with oil.",
            "Grill or bake for 15-20 minutes, turning halfway, until edges are charred.",
            "Alternatively, cook on a stovetop grill pan, turning frequently.",
            "Squeeze fresh lemon juice over the tikka and serve with mint chutney.",
        ],
    }


def aloo_paratha():
    return {
        "name": "Aloo Paratha",
        "category": "North India",
        "ingredients": [
            create_ingredient("Whole Wheat Flour", "2 cups", "250g", "Two cups of fresh whole wheat flour (atta)"),
            create_ingredient("Potatoes", "3 medium", "350g", "Three medium potatoes, boiled and mashed"),
            create_ingredient("Green Chilies", "2", "10g", "Two green chilies, finely chopped"),
            create_ingredient("Onion", "1 small", "80g", "One small onion, finely chopped"),
            create_ingredient("Coriander Leaves", "1/4 cup", "15g", "Quarter cup of fresh coriander leaves, chopped"),
            create_ingredient("Cumin Seeds", "1 tsp", "5g", "One teaspoon of roasted cumin seeds"),
            create_ingredient("Red Chili Powder", "1/2 tsp", "2g", "Half teaspoon of red chili powder"),
            create_ingredient("Amchur Powder", "1 tsp", "5g", "One teaspoon of dry mango powder"),
            create_ingredient("Ghee", "for cooking", "for cooking", "Generous amount of ghee for cooking parathas"),
            create_ingredient("Salt", "to taste", "to taste", "Salt adjusted to preference"),
        ],
        "steps": [
            "Knead whole wheat flour with water and a pinch of salt to make soft, pliable dough. Rest for 30 minutes.",
            "Mix mashed potatoes with green chilies, onion, coriander, cumin, red chili, amchur, and salt.",
            "Divide dough and filling into equal portions (about 8 each).",
            "Roll a dough ball into a small circle, place filling in center.",
            "Gather edges and seal, flatten gently, then roll out carefully into a circle.",
            "Heat a tawa (griddle) on medium-high heat.",
            "Place paratha on hot tawa, cook until bubbles appear, flip.",
            "Apply ghee generously on both sides, pressing edges to cook evenly.",
            "Cook until golden brown spots appear on both sides.",
            "Serve hot with yogurt, pickle, and butter.",
        ],
    }


def rajma_chawal():
    return {
        "name": "Rajma Chawal",
        "category": "North India",
        "ingredients": [
            create_ingredient("Kidney Beans", "1.5 cups", "300g", "One and half cups of dried kidney beans, soaked overnight"),
            create_ingredient("Onions", "2 large", "300g", "Two large onions, finely chopped"),
            create_ingredient("Tomatoes", "3 medium", "300g", "Three medium ripe tomatoes, pureed"),
            create_ingredient("Ginger-Garlic Paste", "2 tbsp", "30g", "Two tablespoons of fresh ginger-garlic paste"),
            create_ingredient("Cumin Seeds", "1 tsp", "5g", "One teaspoon of whole cumin seeds"),
            create_ingredient("Coriander Powder", "1 tbsp", "10g", "One tablespoon of ground coriander"),
            create_ingredient("Red Chili Powder", "1 tsp", "5g", "One teaspoon of red chili powder"),
            create_ingredient("Garam Masala", "1 tsp", "5g", "One teaspoon of garam masala"),
            create_ingredient("Basmati Rice", "2 cups", "400g", "Two cups of aged basmati rice"),
            create_ingredient("Oil", "3 tbsp", "45ml", "Three tablespoons of cooking oil"),
        ],
        "steps": [
            "Pressure cook soaked kidney beans with salt until completely soft, about 25-30 minutes.",
            "Heat oil in a pan, add cumin seeds and let them splutter.",
            "Add onions and fry until golden brown, about 10 minutes.",
            "Add ginger-garlic paste, cook for 2 minutes.",
            "Add tomato puree and cook until oil separates, about 10 minutes.",
            "Add coriander powder, red chili powder, and turmeric. Mix well.",
            "Add cooked rajma with its liquid, mix thoroughly.",
            "Simmer on low heat for 20-30 minutes, mashing some beans for thick gravy.",
            "Add garam masala and fresh coriander before serving.",
            "Cook basmati rice separately and serve rajma over steaming rice.",
        ],
    }


def kadhi_pakora():
    return {
        "name": "Kadhi Pakora",
        "category": "North India",
        "ingredients": [
            create_ingredient("Yogurt", "2 cups", "500g", "Two cups of sour yogurt"),
            create_ingredient("Gram Flour", "1/2 cup", "60g", "Half cup of gram flour (besan)"),
            create_ingredient("Onion", "1 large", "150g", "One large onion for pakoras, sliced thin"),
            create_ingredient("Turmeric", "1/2 tsp", "2g", "Half teaspoon of turmeric powder"),
            create_ingredient("Red Chili Powder", "1 tsp", "5g", "One teaspoon of red chili powder"),
            create_ingredient("Cumin Seeds", "1 tsp", "5g", "One teaspoon of whole cumin seeds"),
            create_ingredient("Fenugreek Seeds", "1/4 tsp", "1g", "Quarter teaspoon of fenugreek seeds"),
            create_ingredient("Dried Red Chilies", "2", "2g", "Two whole dried red chilies"),
            create_ingredient("Curry Leaves", "10-12", "5g", "Ten to twelve fresh curry leaves"),
            create_ingredient("Oil", "for frying", "for frying", "Oil for deep frying pakoras"),
        ],
        "steps": [
            "Whisk yogurt with gram flour and 3 cups water until smooth, no lumps.",
            "For pakoras: Mix 1 cup gram flour, onion slices, green chilies, salt, and water to form thick batter.",
            "Deep fry spoonfuls of batter until golden and crispy. Set aside.",
            "For kadhi: Heat oil in a pan, add cumin, fenugreek seeds, and dried red chilies.",
            "Add curry leaves and asafoetida, let them splutter.",
            "Pour in the yogurt-besan mixture, stirring continuously.",
            "Add turmeric, red chili powder, and salt. Keep stirring to prevent lumps.",
            "Bring to boil, then simmer on low heat for 25-30 minutes, stirring occasionally.",
            "Add fried pakoras to the kadhi 10 minutes before serving.",
            "Temper with ghee, cumin, and red chilies. Serve hot with rice.",
        ],
    }


def tandoori_chicken():
    return {
        "name": "Tandoori Chicken",
        "category": "North India",
        "ingredients": [
            create_ingredient("Chicken", "1 whole", "1.2kg", "One whole chicken, about 1.2kg, cut into pieces with skin"),
            create_ingredient("Yogurt", "1 cup", "250g", "One cup of thick plain yogurt"),
            create_ingredient("Ginger-Garlic Paste", "3 tbsp", "45g", "Three tablespoons of fresh ginger-garlic paste"),
            create_ingredient("Kashmiri Chili Powder", "2 tbsp", "15g", "Two tablespoons of Kashmiri chili for color"),
            create_ingredient("Tandoori Masala", "2 tbsp", "20g", "Two tablespoons of tandoori masala"),
            create_ingredient("Lemon Juice", "3 tbsp", "45ml", "Three tablespoons of fresh lemon juice"),
            create_ingredient("Mustard Oil", "3 tbsp", "45ml", "Three tablespoons of pungent mustard oil"),
            create_ingredient("Kasoori Methi", "1 tbsp", "3g", "One tablespoon of crushed dried fenugreek leaves"),
            create_ingredient("Chaat Masala", "1 tsp", "5g", "One teaspoon of chaat masala for finishing"),
            create_ingredient("Salt", "to taste", "to taste", "Salt adjusted to preference"),
        ],
        "steps": [
            "Make deep cuts in chicken pieces to allow marinade to penetrate.",
            "First marinade: Rub chicken with lemon juice and salt, set aside for 30 minutes.",
            "Mix yogurt, ginger-garlic paste, Kashmiri chili, tandoori masala, mustard oil, and kasoori methi.",
            "Apply this marinade generously over chicken, ensuring it gets into the cuts.",
            "Cover and refrigerate for at least 6 hours, preferably overnight.",
            "Preheat oven to maximum temperature (250°C/480°F) or prepare charcoal grill.",
            "Place chicken on a wire rack over a tray to catch drippings.",
            "Roast for 25-30 minutes, turning once, until charred and cooked through.",
            "Baste with melted butter during last 5 minutes of cooking.",
            "Sprinkle with chaat masala, serve with onion rings and mint chutney.",
        ],
    }


def nihari():
    return {
        "name": "Nihari",
        "category": "North India",
        "ingredients": [
            create_ingredient("Beef Shank", "1 kg", "1000g", "One kilogram of beef shank with bone and marrow"),
            create_ingredient("Onions", "3 large", "450g", "Three large onions, thinly sliced"),
            create_ingredient("Ghee", "1/2 cup", "120g", "Half cup of pure ghee"),
            create_ingredient("Nihari Masala", "3 tbsp", "30g", "Three tablespoons of nihari spice mix"),
            create_ingredient("Wheat Flour", "2 tbsp", "20g", "Two tablespoons of wheat flour for thickening"),
            create_ingredient("Ginger", "3 inch", "30g", "Three-inch piece of ginger, julienned"),
            create_ingredient("Green Chilies", "4", "20g", "Four green chilies, slit lengthwise"),
            create_ingredient("Coriander Leaves", "1/2 cup", "30g", "Half cup of fresh coriander for garnish"),
            create_ingredient("Lemon", "2", "2 pieces", "Two lemons, cut into wedges"),
            create_ingredient("Salt", "to taste", "to taste", "Salt adjusted to preference"),
        ],
        "steps": [
            "Heat ghee in a large heavy pot, fry onions until deep brown and crispy. Remove half for garnish.",
            "Add meat pieces to remaining onions, brown on all sides for 10 minutes.",
            "Add nihari masala, salt, and enough water to cover meat by 2 inches.",
            "Bring to boil, then reduce to lowest heat. Cover tightly.",
            "Simmer for 6-8 hours (traditionally overnight) until meat is falling off bone.",
            "Mix wheat flour with water to make slurry, add to pot, stir well.",
            "Simmer for another 30 minutes until gravy thickens.",
            "The ghee should float on top in a layer.",
            "Serve in deep bowls, topped with fried onions, ginger julienne, green chilies.",
            "Accompany with fresh coriander, lemon wedges, and warm naan.",
        ],
    }



def pav_bhaji():
    return {
        "name": "Pav Bhaji",
        "category": "West India",
        "ingredients": [
            create_ingredient("Potatoes", "4 medium", "400g", "Four medium potatoes, boiled and mashed"),
            create_ingredient("Cauliflower", "1 cup", "150g", "One cup of cauliflower florets, boiled"),
            create_ingredient("Green Peas", "1/2 cup", "75g", "Half cup of green peas, boiled"),
            create_ingredient("Tomatoes", "4 medium", "400g", "Four medium ripe tomatoes, finely chopped"),
            create_ingredient("Onions", "2 large", "300g", "Two large onions, finely chopped"),
            create_ingredient("Capsicum", "1", "100g", "One green capsicum, finely chopped"),
            create_ingredient("Pav Bhaji Masala", "3 tbsp", "30g", "Three tablespoons of pav bhaji masala"),
            create_ingredient("Butter", "6 tbsp", "90g", "Six tablespoons of butter (don't skimp!)"),
            create_ingredient("Pav Buns", "8", "8 pieces", "Eight soft pav buns"),
            create_ingredient("Lemon", "2", "2 pieces", "Two lemons for juice"),
        ],
        "steps": [
            "Boil potatoes, cauliflower, and peas together until very soft. Mash completely.",
            "Heat 3 tbsp butter in a large flat pan (tawa), add onions and sauté until soft.",
            "Add capsicum and cook for 2 minutes.",
            "Add tomatoes and cook until they break down completely, about 10 minutes.",
            "Add pav bhaji masala, turmeric, red chili powder, and salt. Mix well.",
            "Add mashed vegetables, mix thoroughly using a potato masher.",
            "Add water as needed and mash everything together on the tawa.",
            "Keep mashing and cooking for 15-20 minutes, adding butter generously.",
            "Slit pav buns, apply butter, and toast on tawa until golden.",
            "Serve bhaji topped with butter, chopped onions, coriander, and lemon wedge.",
        ],
    }
def vada_pav():
    return {
        "name": "Vada Pav",
        "category": "West India",
        "ingredients": [
            create_ingredient("Potatoes", "4 medium", "400g", "Four medium potatoes, boiled and mashed"),
            create_ingredient("Gram Flour", "1 cup", "120g", "One cup of gram flour (besan) for batter"),
            create_ingredient("Green Chilies", "4", "20g", "Four green chilies, finely chopped"),
            create_ingredient("Garlic", "8 cloves", "25g", "Eight garlic cloves, minced"),
            create_ingredient("Mustard Seeds", "1 tsp", "5g", "One teaspoon of black mustard seeds"),
            create_ingredient("Turmeric", "1/2 tsp", "2g", "Half teaspoon of turmeric powder"),
            create_ingredient("Curry Leaves", "10-12", "5g", "Ten to twelve fresh curry leaves"),
            create_ingredient("Pav Buns", "8", "8 pieces", "Eight fresh pav buns"),
            create_ingredient("Dry Garlic Chutney", "4 tbsp", "40g", "Four tablespoons of dry garlic chutney"),
            create_ingredient("Oil", "for frying", "for frying", "Oil for deep frying vadas"),
        ],
        "steps": [
            "Heat 2 tbsp oil, add mustard seeds, let them splutter.",
            "Add curry leaves, green chilies, and garlic. Sauté for 1 minute.",
            "Add turmeric and mashed potatoes. Mix well, add salt. Let cool.",
            "Shape mixture into round balls slightly smaller than pav size.",
            "Make batter: Mix gram flour, turmeric, red chili, salt, and water to coating consistency.",
            "Heat oil for deep frying to 180°C (350°F).",
            "Dip potato balls in batter, ensuring complete coverage.",
            "Deep fry until golden and crispy, about 3-4 minutes.",
            "Slit pav, spread dry garlic chutney and green chutney inside.",
            "Place hot vada in pav, press gently, serve immediately with fried green chilies.",
        ],
    }
def misal_pav():
    return {
        "name": "Misal Pav",
        "category": "West India",
        "ingredients": [
            create_ingredient("Moth Beans", "1 cup", "200g", "One cup of moth beans (matki), sprouted"),
            create_ingredient("Onions", "2 medium", "200g", "Two medium onions, finely chopped"),
            create_ingredient("Tomatoes", "2 medium", "200g", "Two medium tomatoes, pureed"),
            create_ingredient("Misal Masala", "2 tbsp", "20g", "Two tablespoons of kolhapuri misal masala"),
            create_ingredient("Farsan/Sev", "1 cup", "50g", "One cup of crispy farsan or thin sev"),
            create_ingredient("Tamarind Paste", "1 tbsp", "15g", "One tablespoon of tamarind paste"),
            create_ingredient("Pav Buns", "8", "8 pieces", "Eight soft pav buns"),
            create_ingredient("Coriander Leaves", "1/2 cup", "30g", "Half cup of fresh coriander, chopped"),
            create_ingredient("Lemon", "2", "2 pieces", "Two lemons, cut into wedges"),
            create_ingredient("Oil", "3 tbsp", "45ml", "Three tablespoons of cooking oil"),
        ],
        "steps": [
            "Soak moth beans overnight, then sprout for 1-2 days. Pressure cook until soft.",
            "Heat oil, add mustard seeds, cumin, and curry leaves. Let splutter.",
            "Add onions, sauté until golden brown.",
            "Add tomato puree, cook until oil separates.",
            "Add misal masala, turmeric, and red chili powder. Cook for 2 minutes.",
            "Add sprouted moth beans with some water, tamarind paste, and jaggery.",
            "Simmer for 15-20 minutes until flavors meld and gravy thickens.",
            "Prepare tarri (thin spicy gravy) separately with more water and spices.",
            "Serve misal in bowl, pour tarri over, top generously with farsan.",
            "Add chopped onions, coriander, lemon juice. Serve with buttered pav.",
        ],
    }
def goan_fish_curry():
    return {
        "name": "Goan Fish Curry",
        "category": "West India",
        "ingredients": [
            create_ingredient("Pomfret or Kingfish", "500g", "500g", "Five hundred grams of fresh pomfret or kingfish steaks"),
            create_ingredient("Coconut", "1 cup grated", "100g", "One cup of freshly grated coconut"),
            create_ingredient("Kashmiri Chilies", "6-8", "15g", "Six to eight dried Kashmiri red chilies"),
            create_ingredient("Tamarind", "small ball", "30g", "A small ball of tamarind, soaked"),
            create_ingredient("Onion", "1 large", "150g", "One large onion, sliced"),
            create_ingredient("Garlic", "6 cloves", "20g", "Six cloves of garlic"),
            create_ingredient("Coriander Seeds", "1 tbsp", "10g", "One tablespoon of coriander seeds"),
            create_ingredient("Cumin Seeds", "1 tsp", "5g", "One teaspoon of cumin seeds"),
            create_ingredient("Turmeric", "1/2 tsp", "2g", "Half teaspoon of turmeric powder"),
            create_ingredient("Kokum", "4-5 pieces", "10g", "Four to five pieces of kokum"),
        ],
        "steps": [
            "Clean fish, rub with salt and turmeric. Set aside for 15 minutes.",
            "Soak Kashmiri chilies in warm water for 15 minutes.",
            "Grind coconut, soaked chilies, coriander seeds, cumin, garlic, and turmeric to smooth paste.",
            "Extract tamarind juice by soaking in warm water and squeezing.",
            "Heat oil in a clay pot or pan, add sliced onions, sauté until soft.",
            "Add the ground coconut paste, cook for 5 minutes, stirring.",
            "Add tamarind water, kokum, and 1 cup water. Bring to boil.",
            "Reduce heat, simmer for 10 minutes until oil floats on top.",
            "Gently slide in fish pieces, simmer for 8-10 minutes until fish is cooked.",
            "Do not stir, just shake the pan gently. Serve with steamed rice.",
        ],
    }
def sorpotel():
    return {
        "name": "Sorpotel",
        "category": "West India",
        "ingredients": [
            create_ingredient("Pork", "500g", "500g", "Five hundred grams of pork meat and liver, cubed"),
            create_ingredient("Pork Liver", "200g", "200g", "Two hundred grams of fresh pork liver"),
            create_ingredient("Vinegar", "1/2 cup", "120ml", "Half cup of Goan palm vinegar or white vinegar"),
            create_ingredient("Kashmiri Chilies", "10-12", "25g", "Ten to twelve dried Kashmiri red chilies"),
            create_ingredient("Onions", "2 large", "300g", "Two large onions, finely chopped"),
            create_ingredient("Garlic", "15 cloves", "50g", "Fifteen cloves of garlic"),
            create_ingredient("Ginger", "2 inch", "20g", "Two-inch piece of fresh ginger"),
            create_ingredient("Cumin Seeds", "1 tbsp", "10g", "One tablespoon of cumin seeds"),
            create_ingredient("Black Peppercorns", "1 tsp", "5g", "One teaspoon of black peppercorns"),
            create_ingredient("Cinnamon", "2 inch", "5g", "Two-inch stick of cinnamon"),
        ],
        "steps": [
            "Boil pork and liver separately until cooked. Reserve cooking water. Cut into small pieces.",
            "Soak Kashmiri chilies in vinegar for 30 minutes.",
            "Grind chilies with vinegar, garlic, ginger, cumin, peppercorns, cinnamon, and cloves.",
            "Heat oil, fry onions until golden brown.",
            "Add ground masala paste, cook on low heat for 10 minutes.",
            "Add pork and liver pieces, mix well with the masala.",
            "Add pork stock as needed, simmer for 30 minutes.",
            "Add more vinegar to taste - it should be tangy.",
            "Traditionally, sorpotel tastes better the next day after flavors develop.",
            "Serve with sannas (Goan rice cakes) or pao.",
        ],
    }
def undhiyu():
    return {
        "name": "Undhiyu",
        "category": "West India",
        "ingredients": [
            create_ingredient("Purple Yam", "200g", "200g", "Two hundred grams of purple yam (ratalu), cubed"),
            create_ingredient("Raw Banana", "2", "200g", "Two raw bananas, sliced thick"),
            create_ingredient("Surti Papdi", "1 cup", "150g", "One cup of flat beans (papdi)"),
            create_ingredient("Baby Potatoes", "200g", "200g", "Two hundred grams of baby potatoes"),
            create_ingredient("Sweet Potato", "1 medium", "150g", "One medium sweet potato, cubed"),
            create_ingredient("Green Garlic", "1/2 cup", "50g", "Half cup of green garlic, chopped"),
            create_ingredient("Coriander-Coconut Paste", "1 cup", "150g", "One cup of fresh coriander-coconut-green chili paste"),
            create_ingredient("Methi Muthia", "10-12", "150g", "Ten to twelve fenugreek dumplings"),
            create_ingredient("Oil", "1/2 cup", "120ml", "Half cup of oil for dum cooking"),
            create_ingredient("Ajwain", "1 tsp", "5g", "One teaspoon of carom seeds"),
        ],
        "steps": [
            "Make muthias: Mix gram flour, fenugreek leaves, spices, form into oval dumplings, steam for 15 minutes.",
            "Prepare masala paste: Blend coconut, coriander leaves, green chilies, ginger, and garlic.",
            "Stuff baby potatoes and brinjals with this masala paste.",
            "Layer a heavy pot: Start with oil, then add ajwain and asafoetida.",
            "Layer vegetables: potatoes, yam, sweet potato, raw banana, papdi, brinjals.",
            "Add remaining masala paste, salt, sugar, and a splash of water.",
            "Place muthias on top, drizzle more oil.",
            "Seal pot with dough or tight lid. Cook on very low heat for 45 minutes.",
            "Do not open lid during cooking. Shake pot occasionally.",
            "Serve hot with puri and shrikhand.",
        ],
    }
def dhokla():
    return {
        "name": "Dhokla",
        "category": "West India",
        "ingredients": [
            create_ingredient("Gram Flour", "1 cup", "120g", "One cup of fine gram flour (besan)"),
            create_ingredient("Semolina", "2 tbsp", "20g", "Two tablespoons of fine semolina (rava)"),
            create_ingredient("Yogurt", "1/2 cup", "125g", "Half cup of fresh sour yogurt"),
            create_ingredient("Eno Fruit Salt", "1 tsp", "5g", "One teaspoon of Eno fruit salt"),
            create_ingredient("Sugar", "1 tsp", "5g", "One teaspoon of sugar"),
            create_ingredient("Green Chilies", "2", "10g", "Two green chilies, finely minced"),
            create_ingredient("Mustard Seeds", "1 tsp", "5g", "One teaspoon of black mustard seeds"),
            create_ingredient("Curry Leaves", "10-12", "5g", "Ten to twelve fresh curry leaves"),
            create_ingredient("Oil", "3 tbsp", "45ml", "Three tablespoons of oil"),
            create_ingredient("Coriander", "2 tbsp", "10g", "Two tablespoons of fresh coriander for garnish"),
        ],
        "steps": [
            "Mix gram flour, semolina, yogurt, green chilies, ginger paste, salt, sugar, turmeric.",
            "Add water gradually to make smooth, thick batter. Let rest 15 minutes.",
            "Grease a dhokla plate or thali. Set up steamer with water boiling.",
            "Just before steaming, add Eno and mix quickly - batter will become frothy.",
            "Immediately pour batter into greased plate, spread evenly.",
            "Steam for 15-20 minutes until toothpick comes out clean.",
            "Let cool slightly, cut into squares or diamonds.",
            "For tempering: Heat oil, add mustard seeds, let splutter.",
            "Add curry leaves, green chilies, asafoetida. Pour over dhokla.",
            "Sprinkle with fresh coriander and coconut. Serve with green chutney.",
        ],
    }
def thepla():
    return {
        "name": "Thepla",
        "category": "West India",
        "ingredients": [
            create_ingredient("Whole Wheat Flour", "2 cups", "250g", "Two cups of whole wheat flour"),
            create_ingredient("Gram Flour", "1/4 cup", "30g", "Quarter cup of gram flour"),
            create_ingredient("Fresh Fenugreek Leaves", "1 cup", "60g", "One cup of fresh fenugreek leaves, chopped"),
            create_ingredient("Yogurt", "1/4 cup", "60g", "Quarter cup of fresh yogurt"),
            create_ingredient("Turmeric", "1/2 tsp", "2g", "Half teaspoon of turmeric powder"),
            create_ingredient("Red Chili Powder", "1 tsp", "5g", "One teaspoon of red chili powder"),
            create_ingredient("Cumin Seeds", "1 tsp", "5g", "One teaspoon of cumin seeds"),
            create_ingredient("Sesame Seeds", "1 tbsp", "10g", "One tablespoon of white sesame seeds"),
            create_ingredient("Oil", "3 tbsp + more", "45ml + more", "Three tablespoons oil in dough, more for cooking"),
            create_ingredient("Salt", "to taste", "to taste", "Salt adjusted to preference"),
        ],
        "steps": [
            "Wash and finely chop fenugreek leaves. Squeeze out excess moisture.",
            "Mix wheat flour, gram flour, fenugreek leaves, yogurt, oil, and all spices.",
            "Add turmeric, red chili, cumin, sesame, coriander, salt, sugar.",
            "Knead into soft, pliable dough using water as needed. Rest for 20 minutes.",
            "Divide dough into small balls (about 15-16).",
            "Roll each ball into thin circles, about 6-7 inches diameter.",
            "Heat tawa on medium heat, place thepla, cook until bubbles appear.",
            "Flip, apply oil on cooked side, flip again and apply oil.",
            "Press with spatula to cook evenly. Both sides should have brown spots.",
            "Serve hot with pickle, yogurt, or enjoy plain. Perfect for travel!",
        ],
    }
def laal_maas():
    return {
        "name": "Laal Maas",
        "category": "West India",
        "ingredients": [
            create_ingredient("Mutton", "750g", "750g", "Seven hundred fifty grams of bone-in mutton pieces"),
            create_ingredient("Mathania Chilies", "20-25", "50g", "Twenty to twenty-five dried Mathania red chilies"),
            create_ingredient("Yogurt", "1 cup", "250g", "One cup of thick plain yogurt"),
            create_ingredient("Onions", "3 large", "450g", "Three large onions, sliced thin"),
            create_ingredient("Garlic", "15 cloves", "50g", "Fifteen cloves of garlic"),
            create_ingredient("Ghee", "1/2 cup", "120g", "Half cup of pure desi ghee"),
            create_ingredient("Coriander Seeds", "2 tbsp", "20g", "Two tablespoons of coriander seeds"),
            create_ingredient("Bay Leaves", "3", "3 pieces", "Three dried bay leaves"),
            create_ingredient("Cloves", "6", "2g", "Six whole cloves"),
            create_ingredient("Salt", "to taste", "to taste", "Salt adjusted to preference"),
        ],
        "steps": [
            "Soak Mathania chilies in warm water for 30 minutes. Grind to paste.",
            "Grind garlic and coriander seeds to a coarse paste.",
            "Heat ghee in a heavy pot, add bay leaves and cloves.",
            "Add sliced onions, fry until deep golden brown, about 15 minutes.",
            "Add mutton pieces, brown on high heat for 10 minutes.",
            "Add garlic-coriander paste, cook for 5 minutes.",
            "Add red chili paste - be generous, it should be fiery red!",
            "Add whisked yogurt slowly, stirring continuously.",
            "Add salt and 1 cup water. Cover and simmer on low heat.",
            "Cook for 1.5-2 hours until mutton is tender and oil floats. Serve with bajra roti.",
        ],
    }
def dal_baati_churma():
    return {
        "name": "Dal Baati Churma",
        "category": "West India",
        "ingredients": [
            create_ingredient("Whole Wheat Flour", "2 cups", "250g", "Two cups of coarse whole wheat flour"),
            create_ingredient("Ghee", "1 cup", "240g", "One cup of pure ghee for baati and churma"),
            create_ingredient("Mixed Dals", "1 cup", "200g", "One cup of mixed lentils (chana, moong, toor)"),
            create_ingredient("Semolina", "2 tbsp", "20g", "Two tablespoons of semolina for baati"),
            create_ingredient("Ajwain", "1 tsp", "5g", "One teaspoon of carom seeds"),
            create_ingredient("Coarse Wheat", "1 cup", "150g", "One cup of coarse wheat for churma"),
            create_ingredient("Jaggery", "1/2 cup", "100g", "Half cup of grated jaggery"),
            create_ingredient("Cardamom", "4 pods", "2g", "Four green cardamom pods, powdered"),
            create_ingredient("Onions", "2 medium", "200g", "Two medium onions for dal"),
            create_ingredient("Tomatoes", "2 medium", "200g", "Two medium tomatoes for dal"),
        ],
        "steps": [
            "For Baati: Mix wheat flour, semolina, ajwain, salt, and 4 tbsp ghee. Knead stiff dough.",
            "Shape into round balls (baatis), make a small dent in center.",
            "Bake at 180°C for 30 minutes until hard and golden, or cook on cow dung fire traditionally.",
            "For Dal: Cook mixed dals until soft. Prepare tadka with ghee, cumin, onions, tomatoes, spices.",
            "Add cooked dal to tadka, simmer until thick and flavorful.",
            "For Churma: Crush baked baatis coarsely in mortar.",
            "Mix with melted ghee, powdered jaggery, and cardamom.",
            "Break each baati, crush slightly, dip generously in ghee.",
            "Serve baati swimming in dal, with churma on the side.",
            "The proper way: Pour dal over baati and mix with churma!",
        ],
    }
def masala_dosa():
    return {
        "name": "Masala Dosa",
        "category": "South India",
        "ingredients": [
            create_ingredient("Rice", "3 cups", "600g", "Three cups of raw rice, soaked 6 hours"),
            create_ingredient("Urad Dal", "1 cup", "200g", "One cup of split black gram, soaked 6 hours"),
            create_ingredient("Fenugreek Seeds", "1 tsp", "5g", "One teaspoon of fenugreek seeds, soaked"),
            create_ingredient("Potatoes", "4 large", "500g", "Four large potatoes for filling"),
            create_ingredient("Onions", "2 large", "300g", "Two large onions, sliced"),
            create_ingredient("Mustard Seeds", "1 tsp", "5g", "One teaspoon of black mustard seeds"),
            create_ingredient("Curry Leaves", "15-20", "8g", "Fifteen to twenty fresh curry leaves"),
            create_ingredient("Green Chilies", "4", "20g", "Four green chilies, slit"),
            create_ingredient("Turmeric", "1/2 tsp", "2g", "Half teaspoon of turmeric powder"),
            create_ingredient("Oil", "as needed", "as needed", "Oil for cooking dosas"),
        ],
        "steps": [
            "Grind soaked rice, urad dal, and fenugreek to smooth batter. Add salt.",
            "Ferment batter overnight in warm place until doubled and slightly sour.",
            "For potato filling: Boil potatoes, peel, and mash coarsely.",
            "Heat oil, add mustard seeds, let splutter. Add curry leaves and green chilies.",
            "Add onions, sauté until translucent. Add turmeric and salt.",
            "Add mashed potatoes, mix well. Cook for 5 minutes. Keep warm.",
            "Heat cast iron tawa, sprinkle water, wipe clean.",
            "Pour ladle of batter, spread in circular motion from center outward.",
            "Drizzle oil around edges, cook until golden and crispy.",
            "Place potato filling in center, fold dosa. Serve with sambar and chutneys.",
        ],
    }
def idli_sambar():
    return {
        "name": "Idli Sambar",
        "category": "South India",
        "ingredients": [
            create_ingredient("Idli Rice", "2 cups", "400g", "Two cups of parboiled idli rice"),
            create_ingredient("Urad Dal", "1 cup", "200g", "One cup of whole urad dal"),
            create_ingredient("Toor Dal", "1 cup", "200g", "One cup of split pigeon peas for sambar"),
            create_ingredient("Sambar Powder", "3 tbsp", "25g", "Three tablespoons of homemade sambar powder"),
            create_ingredient("Tamarind", "small ball", "30g", "A small ball of tamarind"),
            create_ingredient("Drumstick", "2", "100g", "Two drumsticks, cut into 3-inch pieces"),
            create_ingredient("Onions", "2 medium", "200g", "Two medium onions, quartered"),
            create_ingredient("Tomatoes", "2 medium", "200g", "Two medium ripe tomatoes, quartered"),
            create_ingredient("Mustard Seeds", "1 tsp", "5g", "One teaspoon of black mustard seeds"),
            create_ingredient("Curry Leaves", "15-20", "8g", "Fifteen to twenty fresh curry leaves"),
        ],
        "steps": [
            "Soak rice and dal separately for 6 hours. Grind dal first until fluffy, then rice.",
            "Mix both batters, add salt. Ferment overnight until doubled.",
            "Grease idli molds, pour batter, steam for 12-15 minutes.",
            "For sambar: Cook toor dal until mushy.",
            "Extract tamarind juice. Cook vegetables in tamarind water until soft.",
            "Add cooked dal, sambar powder, turmeric, and salt. Simmer 15 minutes.",
            "Heat oil, add mustard seeds, curry leaves, dried chilies, asafoetida.",
            "Pour tempering into sambar. Add jaggery to balance flavors.",
            "Let sambar rest for flavors to develop.",
            "Serve hot idlis with sambar and coconut chutney.",
        ],
    }
def vada():
    return {
        "name": "Vada",
        "category": "South India",
        "ingredients": [
            create_ingredient("Urad Dal", "1 cup", "200g", "One cup of whole urad dal, soaked 4 hours"),
            create_ingredient("Green Chilies", "3", "15g", "Three green chilies, chopped fine"),
            create_ingredient("Ginger", "1 inch", "10g", "One-inch piece of ginger, chopped"),
            create_ingredient("Curry Leaves", "10-12", "5g", "Ten to twelve fresh curry leaves, chopped"),
            create_ingredient("Onion", "1 medium", "100g", "One medium onion, finely chopped"),
            create_ingredient("Black Pepper", "1 tsp", "5g", "One teaspoon of coarsely crushed black pepper"),
            create_ingredient("Cumin Seeds", "1 tsp", "5g", "One teaspoon of whole cumin seeds"),
            create_ingredient("Coconut", "2 tbsp", "15g", "Two tablespoons of fresh grated coconut"),
            create_ingredient("Oil", "for frying", "for frying", "Oil for deep frying"),
            create_ingredient("Salt", "to taste", "to taste", "Salt adjusted to preference"),
        ],
        "steps": [
            "Drain soaked dal well. Minimal water is key for fluffy vadas.",
            "Grind dal to thick, fluffy batter. Do not add water while grinding.",
            "Beat batter well with hand to incorporate air - this makes vadas fluffy.",
            "Add green chilies, ginger, curry leaves, onion, pepper, cumin, coconut, salt.",
            "Mix well but don't overmix.",
            "Heat oil to 180°C (350°F). Oil temperature is critical.",
            "Wet hands, take a portion of batter, shape into ball.",
            "Flatten slightly, make a hole in center with wet thumb.",
            "Slide carefully into hot oil. Fry 3-4 vadas at a time.",
            "Fry until golden brown on both sides. Drain and serve hot with sambar and chutney.",
        ],
    }
def chettinad_chicken():
    return {
        "name": "Chettinad Chicken",
        "category": "South India",
        "ingredients": [
            create_ingredient("Chicken", "1 kg", "1000g", "One kilogram of chicken, cut into medium pieces"),
            create_ingredient("Onions", "3 large", "450g", "Three large onions, sliced"),
            create_ingredient("Tomatoes", "2 medium", "200g", "Two medium tomatoes, chopped"),
            create_ingredient("Black Pepper", "2 tbsp", "20g", "Two tablespoons of black peppercorns"),
            create_ingredient("Fennel Seeds", "1 tbsp", "10g", "One tablespoon of fennel seeds"),
            create_ingredient("Dried Red Chilies", "8-10", "20g", "Eight to ten dried red chilies"),
            create_ingredient("Coconut", "1/2 cup", "50g", "Half cup of freshly grated coconut"),
            create_ingredient("Poppy Seeds", "1 tbsp", "10g", "One tablespoon of white poppy seeds"),
            create_ingredient("Curry Leaves", "20-25", "10g", "Twenty to twenty-five fresh curry leaves"),
            create_ingredient("Oil", "4 tbsp", "60ml", "Four tablespoons of gingelly (sesame) oil"),
        ],
        "steps": [
            "Dry roast peppercorns, fennel, dried chilies, poppy seeds until fragrant.",
            "Add grated coconut, roast briefly. Grind to paste with little water.",
            "Heat oil in heavy pan, add curry leaves and sliced onions.",
            "Fry onions until dark brown - this is key for authentic flavor.",
            "Add chicken pieces, brown on high heat for 10 minutes.",
            "Add chopped tomatoes, cook until soft.",
            "Add ground masala paste, salt, and turmeric. Mix well.",
            "Add 1 cup water, cover and cook for 20-25 minutes.",
            "Uncover, cook until chicken is tender and gravy coats the pieces.",
            "Garnish with fresh curry leaves. Serve with rice or parotta.",
        ],
    }
def hyderabadi_biryani():
    return {
        "name": "Hyderabadi Biryani",
        "category": "South India",
        "ingredients": [
            create_ingredient("Basmati Rice", "2 cups", "400g", "Two cups of aged basmati rice, soaked 30 minutes"),
            create_ingredient("Mutton", "750g", "750g", "Seven hundred fifty grams of mutton with bone"),
            create_ingredient("Yogurt", "1 cup", "250g", "One cup of thick whisked yogurt"),
            create_ingredient("Onions", "4 large", "600g", "Four large onions, sliced very thin"),
            create_ingredient("Ghee", "1/2 cup", "120g", "Half cup of pure ghee"),
            create_ingredient("Saffron", "1/4 tsp", "0.5g", "Quarter teaspoon of saffron strands in warm milk"),
            create_ingredient("Mint Leaves", "1 cup", "50g", "One cup of fresh mint leaves"),
            create_ingredient("Coriander", "1 cup", "50g", "One cup of fresh coriander leaves"),
            create_ingredient("Green Chilies", "6", "30g", "Six green chilies, slit"),
            create_ingredient("Biryani Masala", "2 tbsp", "20g", "Two tablespoons of Hyderabadi biryani masala"),
        ],
        "steps": [
            "Fry onions in ghee until deep golden brown. Remove half for layering.",
            "Add mutton to remaining onions, brown well with ginger-garlic paste.",
            "Add yogurt, green chilies, mint, coriander, biryani masala, salt. Mix well.",
            "Cook covered on low heat for 45 minutes until mutton is almost done.",
            "Parboil rice with whole spices until 70% cooked. Drain well.",
            "Layer parboiled rice over mutton. Top with fried onions, saffron milk.",
            "Seal pot with dough. Cook on high heat for 3 minutes.",
            "Reduce to lowest heat, cook for 45 minutes (dum).",
            "Let rest 5 minutes before opening. Gently mix layers while serving.",
            "Serve with raita, mirchi ka salan, and boiled eggs.",
        ],
    }
def pesarattu():
    return {
        "name": "Pesarattu",
        "category": "South India",
        "ingredients": [
            create_ingredient("Green Moong Dal", "1 cup", "200g", "One cup of whole green gram (moong), soaked 6 hours"),
            create_ingredient("Rice", "2 tbsp", "25g", "Two tablespoons of raw rice, soaked with dal"),
            create_ingredient("Green Chilies", "3", "15g", "Three green chilies"),
            create_ingredient("Ginger", "1 inch", "10g", "One-inch piece of fresh ginger"),
            create_ingredient("Cumin Seeds", "1 tsp", "5g", "One teaspoon of cumin seeds"),
            create_ingredient("Onion", "1 medium", "100g", "One medium onion, finely chopped"),
            create_ingredient("Coriander Leaves", "1/4 cup", "15g", "Quarter cup of fresh coriander, chopped"),
            create_ingredient("Oil", "as needed", "as needed", "Oil for cooking pesarattu"),
            create_ingredient("Salt", "to taste", "to taste", "Salt adjusted to preference"),
            create_ingredient("Curry Leaves", "for garnish", "5g", "Fresh curry leaves for garnish"),
        ],
        "steps": [
            "Drain soaked moong dal and rice. Grind with green chilies, ginger, cumin, salt.",
            "Add water gradually to make pourable batter - thinner than dosa batter.",
            "No fermentation needed - pesarattu is made with fresh batter.",
            "Heat flat tawa, sprinkle water, wipe dry.",
            "Pour batter, spread thin from center outward.",
            "Sprinkle chopped onions and coriander on top.",
            "Drizzle oil around edges and on top.",
            "Cook until edges lift and bottom is golden.",
            "Fold and serve hot with ginger chutney (allam pachadi).",
            "For MLA Pesarattu, add upma inside before folding.",
        ],
    }
def appam_with_stew():
    return {
        "name": "Appam with Stew",
        "category": "South India",
        "ingredients": [
            create_ingredient("Raw Rice", "2 cups", "400g", "Two cups of raw rice, soaked overnight"),
            create_ingredient("Coconut", "1 cup", "100g", "One cup of freshly grated coconut"),
            create_ingredient("Yeast", "1/2 tsp", "2g", "Half teaspoon of instant yeast"),
            create_ingredient("Sugar", "1 tbsp", "15g", "One tablespoon of sugar for fermentation"),
            create_ingredient("Chicken", "500g", "500g", "Five hundred grams of chicken for stew"),
            create_ingredient("Coconut Milk", "2 cups", "500ml", "Two cups of thick coconut milk"),
            create_ingredient("Potatoes", "2 medium", "200g", "Two medium potatoes, cubed"),
            create_ingredient("Carrots", "1 medium", "100g", "One medium carrot, cubed"),
            create_ingredient("Green Cardamom", "4 pods", "2g", "Four green cardamom pods"),
            create_ingredient("Cinnamon", "2 inch", "5g", "Two-inch stick of cinnamon"),
        ],
        "steps": [
            "For appam: Grind soaked rice with coconut and cooked rice to smooth batter.",
            "Add yeast, sugar, and salt. Ferment for 6-8 hours until bubbly.",
            "Before cooking, add thin coconut milk to get pouring consistency.",
            "Heat appam pan, pour batter, swirl to coat sides, add more batter in center.",
            "Cover and cook until edges are crispy and center is soft and fluffy.",
            "For stew: Sauté whole spices in coconut oil until fragrant.",
            "Add sliced onions, green chilies, ginger, curry leaves. Cook until soft.",
            "Add chicken and vegetables, sauté for 5 minutes.",
            "Add thin coconut milk, cover and simmer until cooked.",
            "Add thick coconut milk at end, simmer briefly. Serve stew in appam bowls.",
        ],
    }
def kerala_sadya():
    return {
        "name": "Kerala Sadya",
        "category": "South India",
        "ingredients": [
            create_ingredient("Rice", "3 cups", "600g", "Three cups of Kerala matta rice or parboiled rice"),
            create_ingredient("Raw Banana", "2", "200g", "Two raw bananas for kalan and erissery"),
            create_ingredient("Ash Gourd", "200g", "200g", "Two hundred grams of ash gourd for avial"),
            create_ingredient("Drumstick", "2", "100g", "Two drumsticks for sambar"),
            create_ingredient("Yogurt", "2 cups", "500g", "Two cups of fresh thick yogurt for pachadi"),
            create_ingredient("Coconut", "2 cups", "200g", "Two cups of freshly grated coconut"),
            create_ingredient("Jaggery", "1/2 cup", "100g", "Half cup of jaggery for payasam"),
            create_ingredient("Ghee", "1/2 cup", "120g", "Half cup of ghee"),
            create_ingredient("Papadam", "20", "100g", "Twenty pappadams"),
            create_ingredient("Banana Leaf", "4 large", "4 pieces", "Four large banana leaves for serving"),
        ],
        "steps": [
            "This is a feast - prepare multiple dishes: sambar, rasam, avial, thoran, pachadi, olan, kalan, erissery, payasam.",
            "Prepare sambar with mixed vegetables and sambar powder.",
            "Make avial with mixed vegetables in coconut-yogurt gravy.",
            "Prepare thoran: dry stir-fry of vegetables with coconut.",
            "Make pachadi: yogurt-based dish with cucumber or pineapple.",
            "Prepare olan: ash gourd in coconut milk with black-eyed peas.",
            "Make payasam: vermicelli or ada in coconut milk with jaggery.",
            "Prepare pickle, banana chips, papadam, and buttermilk.",
            "Clean banana leaves, soften over flame.",
            "Serve dishes in traditional order on banana leaf. Eat with right hand only!",
        ],
    }
def puliyodarai():
    return {
        "name": "Puliyodarai",
        "category": "South India",
        "ingredients": [
            create_ingredient("Rice", "2 cups", "400g", "Two cups of raw rice, cooked and cooled"),
            create_ingredient("Tamarind", "large ball", "75g", "A large ball of tamarind, soaked"),
            create_ingredient("Sesame Oil", "4 tbsp", "60ml", "Four tablespoons of gingelly (sesame) oil"),
            create_ingredient("Peanuts", "1/4 cup", "40g", "Quarter cup of raw peanuts"),
            create_ingredient("Dried Red Chilies", "6", "15g", "Six dried red chilies"),
            create_ingredient("Mustard Seeds", "1 tsp", "5g", "One teaspoon of black mustard seeds"),
            create_ingredient("Chana Dal", "1 tbsp", "10g", "One tablespoon of split chickpeas"),
            create_ingredient("Urad Dal", "1 tbsp", "10g", "One tablespoon of split black gram"),
            create_ingredient("Fenugreek Seeds", "1/2 tsp", "2g", "Half teaspoon of fenugreek seeds"),
            create_ingredient("Turmeric", "1/2 tsp", "2g", "Half teaspoon of turmeric powder"),
        ],
        "steps": [
            "Extract thick tamarind juice by soaking in warm water and squeezing.",
            "Dry roast fenugreek, coriander seeds, red chilies. Grind to powder.",
            "Heat sesame oil, fry peanuts until golden. Remove.",
            "In same oil, add mustard seeds, let splutter.",
            "Add chana dal, urad dal, dried chilies, curry leaves. Fry until golden.",
            "Add tamarind extract, turmeric, salt, and jaggery.",
            "Cook on medium heat until mixture thickens and oil separates.",
            "Add ground spice powder, mix well. This is the puliyodarai paste.",
            "Mix paste with cooked cooled rice and fried peanuts.",
            "Traditionally offered in temples. Perfect for travel as it stays fresh.",
        ],
    }
def rasam():
    return {
        "name": "Rasam",
        "category": "South India",
        "ingredients": [
            create_ingredient("Toor Dal", "1/4 cup", "50g", "Quarter cup of cooked and mashed toor dal"),
            create_ingredient("Tomatoes", "2 medium", "200g", "Two medium ripe tomatoes, crushed"),
            create_ingredient("Tamarind", "small ball", "20g", "A small ball of tamarind"),
            create_ingredient("Rasam Powder", "2 tbsp", "15g", "Two tablespoons of homemade rasam powder"),
            create_ingredient("Black Pepper", "1 tsp", "5g", "One teaspoon of crushed black pepper"),
            create_ingredient("Cumin Seeds", "1 tsp", "5g", "One teaspoon of cumin seeds"),
            create_ingredient("Mustard Seeds", "1/2 tsp", "2g", "Half teaspoon of black mustard seeds"),
            create_ingredient("Garlic", "4 cloves", "12g", "Four cloves of garlic, crushed"),
            create_ingredient("Curry Leaves", "10-12", "5g", "Ten to twelve fresh curry leaves"),
            create_ingredient("Coriander Leaves", "2 tbsp", "10g", "Two tablespoons of fresh coriander"),
        ],
        "steps": [
            "Extract tamarind juice by soaking in warm water.",
            "Mix tamarind water with crushed tomatoes, rasam powder, turmeric, salt.",
            "Add 2 cups water, bring to boil on medium heat.",
            "Add cooked dal, crushed pepper, and crushed garlic.",
            "Let it come to a frothy boil - do not over-boil or it loses flavor.",
            "Prepare tempering: Heat ghee, add mustard seeds, cumin.",
            "When they splutter, add dried red chilies and curry leaves.",
            "Pour tempering into rasam.",
            "Add fresh coriander leaves, cover immediately.",
            "Serve hot with rice or drink in small cups. Healing for cold and flu!",
        ],
    }
def macher_jhol():
    return {
        "name": "Macher Jhol",
        "category": "East India",
        "ingredients": [
            create_ingredient("Rohu Fish", "500g", "500g", "Five hundred grams of rohu fish, cut into steaks"),
            create_ingredient("Potatoes", "2 medium", "200g", "Two medium potatoes, quartered"),
            create_ingredient("Tomatoes", "2 medium", "200g", "Two medium ripe tomatoes, quartered"),
            create_ingredient("Onion", "1 large", "150g", "One large onion, sliced"),
            create_ingredient("Mustard Oil", "4 tbsp", "60ml", "Four tablespoons of pungent mustard oil"),
            create_ingredient("Turmeric", "1 tsp", "5g", "One teaspoon of turmeric powder"),
            create_ingredient("Cumin Powder", "1 tsp", "5g", "One teaspoon of roasted cumin powder"),
            create_ingredient("Green Chilies", "4", "20g", "Four green chilies, slit"),
            create_ingredient("Nigella Seeds", "1/2 tsp", "2g", "Half teaspoon of nigella seeds (kalonji)"),
            create_ingredient("Coriander Leaves", "2 tbsp", "10g", "Two tablespoons of fresh coriander"),
        ],
        "steps": [
            "Rub fish pieces with turmeric and salt. Set aside for 15 minutes.",
            "Heat mustard oil until smoking, then reduce heat slightly.",
            "Fry fish pieces until light golden on both sides. Remove carefully.",
            "In same oil, add nigella seeds, let splutter.",
            "Add potatoes, fry until light brown on edges.",
            "Add onions, sauté until softened.",
            "Add tomatoes, turmeric, cumin, salt. Cook until tomatoes soften.",
            "Add 2 cups water, bring to boil. Simmer until potatoes are cooked.",
            "Gently slide in fried fish and green chilies.",
            "Simmer for 5 minutes. Garnish with coriander. Serve with steamed rice.",
        ],
    }
def shorshe_ilish():
    return {
        "name": "Shorshe Ilish",
        "category": "East India",
        "ingredients": [
            create_ingredient("Hilsa Fish", "500g", "500g", "Five hundred grams of fresh hilsa fish steaks"),
            create_ingredient("Mustard Seeds", "3 tbsp", "30g", "Three tablespoons of yellow and black mustard seeds"),
            create_ingredient("Green Chilies", "6", "30g", "Six green chilies"),
            create_ingredient("Mustard Oil", "4 tbsp", "60ml", "Four tablespoons of raw mustard oil"),
            create_ingredient("Turmeric", "1 tsp", "5g", "One teaspoon of turmeric powder"),
            create_ingredient("Nigella Seeds", "1/2 tsp", "2g", "Half teaspoon of nigella seeds"),
            create_ingredient("Salt", "to taste", "to taste", "Salt adjusted to preference"),
            create_ingredient("Water", "1 cup", "250ml", "One cup of water"),
            create_ingredient("Poppy Seeds", "1 tbsp", "10g", "One tablespoon of poppy seeds, optional"),
            create_ingredient("Coconut", "2 tbsp", "15g", "Two tablespoons of grated coconut, optional"),
        ],
        "steps": [
            "Soak mustard seeds in water for 30 minutes.",
            "Grind mustard with green chilies, salt, and a little water to fine paste.",
            "Rub fish with turmeric and salt. Set aside for 10 minutes.",
            "Heat mustard oil until smoking point, let cool slightly.",
            "Fry fish lightly on both sides (optional - can skip for softer texture).",
            "In the same oil, add nigella seeds.",
            "Add mustard paste diluted with water. Bring to simmer.",
            "Add remaining green chilies and turmeric.",
            "Place fish steaks in the gravy, spoon gravy over them.",
            "Cover and cook on low heat for 10-12 minutes. Drizzle raw mustard oil. Serve with rice.",
        ],
    }
def chingri_malai_curry():
    return {
        "name": "Chingri Malai Curry",
        "category": "East India",
        "ingredients": [
            create_ingredient("Prawns", "500g", "500g", "Five hundred grams of large prawns, cleaned"),
            create_ingredient("Coconut Milk", "1.5 cups", "375ml", "One and half cups of thick coconut milk"),
            create_ingredient("Onion Paste", "1 cup", "150g", "One cup of smooth onion paste"),
            create_ingredient("Ginger Paste", "1 tbsp", "15g", "One tablespoon of fresh ginger paste"),
            create_ingredient("Turmeric", "1/2 tsp", "2g", "Half teaspoon of turmeric powder"),
            create_ingredient("Green Chilies", "3", "15g", "Three green chilies, slit"),
            create_ingredient("Sugar", "1 tsp", "5g", "One teaspoon of sugar"),
            create_ingredient("Ghee", "3 tbsp", "45g", "Three tablespoons of ghee"),
            create_ingredient("Bay Leaves", "2", "2g", "Two bay leaves"),
            create_ingredient("Cardamom", "3 pods", "1.5g", "Three green cardamom pods"),
        ],
        "steps": [
            "Clean prawns, devein, keep tails intact. Marinate with turmeric and salt.",
            "Heat ghee, fry prawns lightly until pink. Remove and set aside.",
            "In same ghee, add bay leaves, cardamom, cinnamon.",
            "Add onion paste, fry until golden brown, about 10 minutes.",
            "Add ginger paste, cook for 2 minutes.",
            "Add turmeric, red chili powder, and salt. Mix well.",
            "Pour in coconut milk, bring to gentle simmer. Do not boil vigorously.",
            "Add fried prawns and green chilies.",
            "Simmer on low heat for 5-7 minutes.",
            "Add sugar to balance. Serve with steamed basmati rice.",
        ],
    }
def pakhala_bhata():
    return {
        "name": "Pakhala Bhata",
        "category": "East India",
        "ingredients": [
            create_ingredient("Cooked Rice", "3 cups", "600g", "Three cups of cooled cooked rice"),
            create_ingredient("Water", "4 cups", "1 liter", "Four cups of water"),
            create_ingredient("Curd", "1/2 cup", "125g", "Half cup of fresh curd (optional for jeera pakhala)"),
            create_ingredient("Green Chilies", "3", "15g", "Three green chilies, crushed"),
            create_ingredient("Cucumber", "1 medium", "150g", "One medium cucumber, diced"),
            create_ingredient("Onion", "1 small", "80g", "One small onion, sliced"),
            create_ingredient("Fried Fish", "200g", "200g", "Two hundred grams of fried fish for accompaniment"),
            create_ingredient("Cumin Seeds", "1 tsp", "5g", "One teaspoon of cumin seeds for tadka"),
            create_ingredient("Curry Leaves", "10", "5g", "Ten fresh curry leaves"),
            create_ingredient("Salt", "to taste", "to taste", "Salt adjusted to preference"),
        ],
        "steps": [
            "Use leftover rice or cook fresh rice and let it cool completely.",
            "Place rice in a large clay pot or bowl.",
            "Add water to cover rice by 2 inches. Add salt.",
            "For fermented version: Cover and let sit overnight in warm place.",
            "For quick version: Add curd to water-rice mixture.",
            "Prepare tadka: Heat oil, add cumin, dried chilies, curry leaves.",
            "Pour tadka over pakhala.",
            "Add crushed green chilies, sliced onions, cucumber.",
            "Serve cold or at room temperature.",
            "Accompaniments: Fried fish, badi chura, saga bhaja, aloo bharta.",
        ],
    }
def dalma():
    return {
        "name": "Dalma",
        "category": "East India",
        "ingredients": [
            create_ingredient("Chana Dal", "1 cup", "200g", "One cup of split chickpeas"),
            create_ingredient("Raw Banana", "1", "100g", "One raw banana, cubed"),
            create_ingredient("Papaya", "1 cup", "150g", "One cup of raw papaya, cubed"),
            create_ingredient("Drumstick", "2", "100g", "Two drumsticks, cut into pieces"),
            create_ingredient("Pumpkin", "1 cup", "150g", "One cup of pumpkin, cubed"),
            create_ingredient("Brinjal", "1 medium", "100g", "One medium brinjal, cubed"),
            create_ingredient("Coconut", "1/2 cup", "50g", "Half cup of freshly grated coconut"),
            create_ingredient("Panch Phoran", "1 tsp", "5g", "One teaspoon of panch phoran (five-spice mix)"),
            create_ingredient("Ghee", "3 tbsp", "45g", "Three tablespoons of ghee"),
            create_ingredient("Dried Red Chilies", "2", "5g", "Two dried red chilies"),
        ],
        "steps": [
            "Pressure cook chana dal with turmeric until soft but not mushy.",
            "Add all vegetables to the dal, cook until tender but not overcooked.",
            "The vegetables should hold their shape.",
            "Add salt, sugar (traditional), and grated coconut.",
            "Heat ghee for tempering, add panch phoran.",
            "When seeds splutter, add dried red chilies.",
            "Pour tempering over the dalma.",
            "Traditional Jagannath temple prasad - no onion or garlic.",
            "Consistency should be thick, not runny.",
            "Serve hot with steamed rice. A staple of Odia cuisine.",
        ],
    }
def litti_chokha():
    return {
        "name": "Litti Chokha",
        "category": "East India",
        "ingredients": [
            create_ingredient("Whole Wheat Flour", "2 cups", "250g", "Two cups of whole wheat flour"),
            create_ingredient("Sattu", "1 cup", "150g", "One cup of roasted gram flour (sattu)"),
            create_ingredient("Onion", "1 medium", "100g", "One medium onion, finely chopped for sattu"),
            create_ingredient("Green Chilies", "3", "15g", "Three green chilies, chopped"),
            create_ingredient("Ajwain", "1 tsp", "5g", "One teaspoon of carom seeds"),
            create_ingredient("Brinjal", "2 large", "300g", "Two large brinjals for chokha"),
            create_ingredient("Tomatoes", "2 medium", "200g", "Two medium tomatoes for chokha"),
            create_ingredient("Ghee", "1/2 cup", "120g", "Half cup of ghee for dipping"),
            create_ingredient("Mustard Oil", "3 tbsp", "45ml", "Three tablespoons of mustard oil"),
            create_ingredient("Garlic", "6 cloves", "20g", "Six cloves of garlic, minced"),
        ],
        "steps": [
            "For sattu filling: Mix sattu with chopped onions, green chilies, coriander, garlic, ajwain, mustard oil, salt, lime juice.",
            "For dough: Mix wheat flour, ajwain, ghee, salt. Knead stiff dough with water.",
            "Divide dough into balls. Flatten, place sattu filling, seal and shape round.",
            "Traditionally bake over cow dung cakes or charcoal until charred spots appear.",
            "Alternatively, bake at 200°C for 25-30 minutes, then char on open flame.",
            "For chokha: Roast brinjal and tomatoes over direct flame until charred.",
            "Peel and mash roasted vegetables.",
            "Add chopped onions, garlic, green chilies, coriander, mustard oil, salt.",
            "Break hot litti, dunk generously in melted ghee.",
            "Serve litti soaked in ghee with baingan and tomato chokha.",
        ],
    }
def ghugni():
    return {
        "name": "Ghugni",
        "category": "East India",
        "ingredients": [
            create_ingredient("Dried Yellow Peas", "1 cup", "200g", "One cup of dried yellow/white peas, soaked overnight"),
            create_ingredient("Potatoes", "2 medium", "200g", "Two medium potatoes, diced small"),
            create_ingredient("Onions", "2 medium", "200g", "Two medium onions, finely chopped"),
            create_ingredient("Tomatoes", "2 medium", "200g", "Two medium tomatoes, chopped"),
            create_ingredient("Ginger", "1 inch", "10g", "One-inch piece of ginger, minced"),
            create_ingredient("Green Chilies", "2", "10g", "Two green chilies, slit"),
            create_ingredient("Cumin Seeds", "1 tsp", "5g", "One teaspoon of cumin seeds"),
            create_ingredient("Mustard Oil", "3 tbsp", "45ml", "Three tablespoons of mustard oil"),
            create_ingredient("Tamarind", "small ball", "15g", "A small piece of tamarind for tanginess"),
            create_ingredient("Fresh Coconut", "2 tbsp", "15g", "Two tablespoons of grated coconut for topping"),
        ],
        "steps": [
            "Boil soaked peas with salt until tender but not mushy. Drain, reserve water.",
            "Heat mustard oil until smoking, then let cool slightly.",
            "Add cumin seeds, let splutter. Add bay leaf.",
            "Add onions, fry until golden brown.",
            "Add ginger, garlic, green chilies. Sauté for 2 minutes.",
            "Add tomatoes, cook until soft.",
            "Add turmeric, red chili powder, cumin powder, salt.",
            "Add boiled peas and potatoes. Add reserved water as needed.",
            "Simmer until potatoes are cooked and gravy thickens.",
            "Top with fresh coconut, chopped onions, coriander, green chilies. Serve with puffed rice.",
        ],
    }
def momos():
    return {
        "name": "Momos",
        "category": "East India",
        "ingredients": [
            create_ingredient("All-Purpose Flour", "2 cups", "250g", "Two cups of all-purpose flour for wrappers"),
            create_ingredient("Chicken Mince", "300g", "300g", "Three hundred grams of chicken mince"),
            create_ingredient("Cabbage", "1 cup", "100g", "One cup of finely chopped cabbage"),
            create_ingredient("Onions", "1 medium", "100g", "One medium onion, finely chopped"),
            create_ingredient("Ginger", "1 tbsp", "15g", "One tablespoon of minced ginger"),
            create_ingredient("Garlic", "1 tbsp", "15g", "One tablespoon of minced garlic"),
            create_ingredient("Soy Sauce", "2 tbsp", "30ml", "Two tablespoons of soy sauce"),
            create_ingredient("Green Onions", "1/4 cup", "20g", "Quarter cup of chopped green onions"),
            create_ingredient("Oil", "2 tbsp", "30ml", "Two tablespoons of oil"),
            create_ingredient("Black Pepper", "1/2 tsp", "2g", "Half teaspoon of black pepper"),
        ],
        "steps": [
            "Make dough: Mix flour with warm water, knead until smooth. Rest 30 minutes covered.",
            "For filling: Mix mince with cabbage, onion, ginger, garlic, soy sauce, pepper, oil.",
            "Add chopped green onions and salt. Mix well but don't overwork.",
            "Roll small portions of dough into thin circles, about 3 inches.",
            "Place filling in center, pleat edges to seal in half-moon or round shape.",
            "Traditional shapes: round with pleated top, or half-moon.",
            "Set up steamer with water boiling. Line with cabbage leaves or parchment.",
            "Place momos without touching, steam for 12-15 minutes.",
            "For tomato chutney: Blend roasted tomatoes, chilies, garlic, ginger.",
            "Serve hot with fiery red chutney and clear soup.",
        ],
    }
def thukpa():
    return {
        "name": "Thukpa",
        "category": "East India",
        "ingredients": [
            create_ingredient("Noodles", "200g", "200g", "Two hundred grams of thukpa noodles or any wheat noodles"),
            create_ingredient("Chicken", "250g", "250g", "Two hundred fifty grams of chicken, sliced thin"),
            create_ingredient("Chicken Stock", "6 cups", "1.5 liters", "Six cups of rich chicken stock"),
            create_ingredient("Cabbage", "1 cup", "100g", "One cup of shredded cabbage"),
            create_ingredient("Carrots", "1 medium", "100g", "One medium carrot, julienned"),
            create_ingredient("Onion", "1 medium", "100g", "One medium onion, sliced"),
            create_ingredient("Ginger", "1 tbsp", "15g", "One tablespoon of minced ginger"),
            create_ingredient("Garlic", "1 tbsp", "15g", "One tablespoon of minced garlic"),
            create_ingredient("Green Onions", "1/4 cup", "20g", "Quarter cup of chopped green onions"),
            create_ingredient("Chili Sauce", "2 tbsp", "30ml", "Two tablespoons of Sichuan chili sauce"),
        ],
        "steps": [
            "Boil noodles according to package directions. Drain, rinse, set aside.",
            "Heat oil in large pot, add sliced chicken, stir-fry until browned.",
            "Add onions, ginger, garlic. Sauté until fragrant.",
            "Add carrots and cabbage, stir-fry for 2 minutes.",
            "Pour in chicken stock, bring to boil.",
            "Season with soy sauce, salt, pepper.",
            "Simmer for 10 minutes until vegetables are tender.",
            "Add more vegetables: bok choy, mushrooms if desired.",
            "Place cooked noodles in serving bowls.",
            "Ladle hot soup over noodles. Top with green onions, chili sauce, cilantro.",
        ],
    }
def sel_roti():
    return {
        "name": "Sel Roti",
        "category": "East India",
        "ingredients": [
            create_ingredient("Rice", "2 cups", "400g", "Two cups of rice, soaked overnight"),
            create_ingredient("Sugar", "1/2 cup", "100g", "Half cup of sugar"),
            create_ingredient("Ghee", "3 tbsp", "45g", "Three tablespoons of melted ghee"),
            create_ingredient("Cardamom", "4 pods", "2g", "Four green cardamom pods, powdered"),
            create_ingredient("Banana", "1 small ripe", "80g", "One small ripe banana (optional)"),
            create_ingredient("Coconut", "2 tbsp", "15g", "Two tablespoons of grated coconut (optional)"),
            create_ingredient("Cloves", "2", "1g", "Two cloves, powdered"),
            create_ingredient("Milk", "1/4 cup", "60ml", "Quarter cup of milk"),
            create_ingredient("Oil", "for frying", "for frying", "Oil for deep frying"),
            create_ingredient("Salt", "pinch", "pinch", "A pinch of salt"),
        ],
        "steps": [
            "Drain soaked rice. Grind to smooth paste with sugar, milk, ghee.",
            "Add cardamom, clove powder, mashed banana if using.",
            "Batter should be thick but pourable - thicker than dosa batter.",
            "Let batter rest for 30 minutes.",
            "Heat oil in kadai for deep frying. Test with a drop of batter.",
            "Take batter in hand, let it flow in circular motion into hot oil.",
            "Traditional shape is a ring - like a thick donut.",
            "Fry until golden brown on one side, flip carefully.",
            "Fry other side until golden and crispy.",
            "Drain on paper. Serve warm with yogurt or as is. Traditional Nepali festive bread.",
        ],
    }
def poha():
    return {
        "name": "Poha",
        "category": "Central India",
        "ingredients": [
            create_ingredient("Flattened Rice (Poha)", "2 cups", "150g", "Two cups of medium thickness flattened rice"),
            create_ingredient("Onion", "1 large", "150g", "One large onion, finely chopped"),
            create_ingredient("Potatoes", "2 medium", "200g", "Two medium potatoes, diced small"),
            create_ingredient("Green Chilies", "2", "10g", "Two green chilies, chopped"),
            create_ingredient("Peanuts", "1/4 cup", "40g", "Quarter cup of raw peanuts"),
            create_ingredient("Mustard Seeds", "1 tsp", "5g", "One teaspoon of black mustard seeds"),
            create_ingredient("Curry Leaves", "10-12", "5g", "Ten to twelve fresh curry leaves"),
            create_ingredient("Turmeric", "1/2 tsp", "2g", "Half teaspoon of turmeric powder"),
            create_ingredient("Lemon", "1", "1 piece", "One lemon for juice"),
            create_ingredient("Oil", "3 tbsp", "45ml", "Three tablespoons of cooking oil"),
        ],
        "steps": [
            "Rinse poha gently in colander, let drain. It should be moist, not soggy.",
            "Add turmeric, salt, sugar to poha, mix gently. Set aside.",
            "Heat oil, add mustard seeds, let them splutter.",
            "Add peanuts, fry until golden. Add curry leaves.",
            "Add diced potatoes, cover and cook until tender.",
            "Add onions and green chilies, sauté until onions are soft.",
            "Add the prepared poha, mix gently to avoid breaking.",
            "Cook for 3-4 minutes, stirring occasionally.",
            "Squeeze lemon juice, add chopped coriander.",
            "Serve hot, garnished with sev and fresh coriander. Classic Indore breakfast!",
        ],
    }
def bhutte_ka_kees():
    return {
        "name": "Bhutte Ka Kees",
        "category": "Central India",
        "ingredients": [
            create_ingredient("Fresh Corn", "4 cobs", "400g", "Four fresh corn cobs, kernels removed and grated"),
            create_ingredient("Milk", "1 cup", "250ml", "One cup of full-fat milk"),
            create_ingredient("Ghee", "3 tbsp", "45g", "Three tablespoons of ghee"),
            create_ingredient("Cumin Seeds", "1 tsp", "5g", "One teaspoon of cumin seeds"),
            create_ingredient("Green Chilies", "2", "10g", "Two green chilies, finely chopped"),
            create_ingredient("Ginger", "1 inch", "10g", "One-inch piece of ginger, grated"),
            create_ingredient("Turmeric", "1/4 tsp", "1g", "Quarter teaspoon of turmeric"),
            create_ingredient("Sugar", "1 tsp", "5g", "One teaspoon of sugar"),
            create_ingredient("Coriander Leaves", "2 tbsp", "10g", "Two tablespoons of fresh coriander"),
            create_ingredient("Salt", "to taste", "to taste", "Salt adjusted to preference"),
        ],
        "steps": [
            "Grate fresh corn kernels to get coarse paste with milky juice.",
            "Heat ghee in a pan, add cumin seeds.",
            "When cumin splutters, add green chilies and ginger.",
            "Add grated corn, stir well on medium heat.",
            "Add turmeric, salt, and sugar.",
            "Pour in milk, mix well.",
            "Cook on low heat, stirring frequently to prevent sticking.",
            "Cook for 15-20 minutes until mixture thickens and corn is cooked.",
            "The texture should be creamy but not runny.",
            "Garnish with coriander and serve hot. Indore monsoon specialty!",
        ],
    }
def sabudana_khichdi():
    return {
        "name": "Sabudana Khichdi",
        "category": "Central India",
        "ingredients": [
            create_ingredient("Sabudana (Tapioca Pearls)", "1 cup", "150g", "One cup of tapioca pearls, soaked overnight"),
            create_ingredient("Peanuts", "1/2 cup", "75g", "Half cup of roasted peanuts, coarsely crushed"),
            create_ingredient("Potatoes", "2 medium", "200g", "Two medium potatoes, cubed small"),
            create_ingredient("Green Chilies", "2", "10g", "Two green chilies, chopped"),
            create_ingredient("Cumin Seeds", "1 tsp", "5g", "One teaspoon of cumin seeds"),
            create_ingredient("Curry Leaves", "10", "5g", "Ten fresh curry leaves"),
            create_ingredient("Ghee", "3 tbsp", "45g", "Three tablespoons of ghee or peanut oil"),
            create_ingredient("Sugar", "1 tsp", "5g", "One teaspoon of sugar"),
            create_ingredient("Lemon Juice", "2 tbsp", "30ml", "Two tablespoons of fresh lemon juice"),
            create_ingredient("Sendha Namak", "to taste", "to taste", "Rock salt for fasting"),
        ],
        "steps": [
            "Soak sabudana in just enough water to cover, for 6-8 hours or overnight.",
            "Pearls should be soft and separate, not mushy or sticky.",
            "Drain any excess water. Add crushed peanuts and mix.",
            "Heat ghee in non-stick pan, add cumin seeds.",
            "Add curry leaves and cubed potatoes.",
            "Cover and cook potatoes until tender, stirring occasionally.",
            "Add green chilies, soaked sabudana, sugar, and rock salt.",
            "Mix gently, cook on medium heat for 5-7 minutes.",
            "Sabudana should turn translucent when cooked.",
            "Add lemon juice and coriander. Serve hot. Perfect for Navratri fasting!",
        ],
    }
def indori_sev():
    return {
        "name": "Indori Sev",
        "category": "Central India",
        "ingredients": [
            create_ingredient("Gram Flour", "2 cups", "200g", "Two cups of fine gram flour (besan)"),
            create_ingredient("Red Chili Powder", "1 tbsp", "10g", "One tablespoon of red chili powder"),
            create_ingredient("Turmeric", "1/4 tsp", "1g", "Quarter teaspoon of turmeric"),
            create_ingredient("Carom Seeds", "1/2 tsp", "2g", "Half teaspoon of carom seeds (ajwain)"),
            create_ingredient("Hot Oil", "2 tbsp", "30ml", "Two tablespoons of hot oil for dough"),
            create_ingredient("Black Pepper", "1/2 tsp", "2g", "Half teaspoon of black pepper"),
            create_ingredient("Asafoetida", "pinch", "0.5g", "A pinch of asafoetida (hing)"),
            create_ingredient("Oil", "for frying", "for frying", "Oil for deep frying"),
            create_ingredient("Salt", "to taste", "to taste", "Salt adjusted to preference"),
            create_ingredient("Baking Soda", "pinch", "pinch", "A pinch of baking soda for crispiness"),
        ],
        "steps": [
            "Sift gram flour to remove lumps.",
            "Add turmeric, red chili, pepper, carom seeds, asafoetida, salt, baking soda.",
            "Add hot oil to flour, mix well (this makes sev crispy).",
            "Gradually add water to make stiff but pliable dough.",
            "Heat oil for deep frying to 180°C (350°F).",
            "Fill sev press with dough, use fine-hole disc for thin sev.",
            "Press directly over hot oil in circular motion.",
            "Fry until bubbling stops and sev is golden.",
            "Remove, drain on paper towels.",
            "Cool completely before storing. Sprinkle on poha, use in chaat, or eat plain!",
        ],
    }
def dal_pithi():
    return {
        "name": "Dal Pithi",
        "category": "Central India",
        "ingredients": [
            create_ingredient("Chana Dal", "1/2 cup", "100g", "Half cup of split chickpeas"),
            create_ingredient("Moong Dal", "1/2 cup", "100g", "Half cup of split mung beans"),
            create_ingredient("Wheat Flour", "1 cup", "125g", "One cup of whole wheat flour for pithis"),
            create_ingredient("Onion", "1 medium", "100g", "One medium onion, sliced"),
            create_ingredient("Tomatoes", "2 medium", "200g", "Two medium tomatoes, chopped"),
            create_ingredient("Ghee", "3 tbsp", "45g", "Three tablespoons of ghee"),
            create_ingredient("Cumin Seeds", "1 tsp", "5g", "One teaspoon of cumin seeds"),
            create_ingredient("Turmeric", "1/2 tsp", "2g", "Half teaspoon of turmeric"),
            create_ingredient("Red Chili Powder", "1 tsp", "5g", "One teaspoon of red chili powder"),
            create_ingredient("Coriander", "2 tbsp", "10g", "Two tablespoons of fresh coriander"),
        ],
        "steps": [
            "For pithis: Make stiff dough with wheat flour, salt, and water. Rest 15 minutes.",
            "Roll into thin rope, cut into small pieces, flatten into rough discs.",
            "Boil dals together until completely soft and mushy.",
            "Heat ghee, add cumin seeds, let splutter.",
            "Add onions, fry until golden.",
            "Add tomatoes, cook until soft.",
            "Add turmeric, red chili, coriander powder, salt.",
            "Add cooked dal and water to make thin consistency.",
            "Bring to boil, add pithis one by one.",
            "Simmer until pithis are cooked through, about 15 minutes. Serve hot with ghee.",
        ],
    }
def khopra_patties():
    return {
        "name": "Khopra Patties",
        "category": "Central India",
        "ingredients": [
            create_ingredient("Potatoes", "500g", "500g", "Five hundred grams of potatoes, boiled and mashed"),
            create_ingredient("Fresh Coconut", "1 cup", "100g", "One cup of fresh grated coconut"),
            create_ingredient("Green Chilies", "2", "10g", "Two green chilies, minced"),
            create_ingredient("Coriander Leaves", "1/4 cup", "15g", "Quarter cup of fresh coriander, chopped"),
            create_ingredient("Raisins", "2 tbsp", "20g", "Two tablespoons of raisins"),
            create_ingredient("Sugar", "2 tbsp", "25g", "Two tablespoons of sugar"),
            create_ingredient("Bread Crumbs", "1 cup", "60g", "One cup of bread crumbs for coating"),
            create_ingredient("Oil", "for frying", "for frying", "Oil for shallow frying"),
            create_ingredient("Ginger", "1 inch", "10g", "One-inch ginger, grated"),
            create_ingredient("Salt", "to taste", "to taste", "Salt adjusted to preference"),
        ],
        "steps": [
            "Mix mashed potatoes with salt and a little cornflour to bind.",
            "For filling: Mix coconut, green chilies, coriander, raisins, sugar, ginger.",
            "Divide potato mixture and coconut filling into equal portions.",
            "Take potato portion, flatten in palm, place filling in center.",
            "Seal edges and shape into oval patties.",
            "Roll in bread crumbs, pressing gently to adhere.",
            "Heat oil for shallow frying.",
            "Fry patties until golden brown on both sides.",
            "Drain on paper towels.",
            "Serve hot with tamarind and coriander chutney. Sweet and savory delight!",
        ],
    }
def bafla():
    return {
        "name": "Bafla",
        "category": "Central India",
        "ingredients": [
            create_ingredient("Wheat Flour", "2 cups", "250g", "Two cups of coarse whole wheat flour"),
            create_ingredient("Semolina", "2 tbsp", "20g", "Two tablespoons of semolina"),
            create_ingredient("Ghee", "3/4 cup", "180g", "Three-quarter cup of ghee (for dough and dipping)"),
            create_ingredient("Salt", "1/2 tsp", "3g", "Half teaspoon of salt"),
            create_ingredient("Ajwain", "1/2 tsp", "2g", "Half teaspoon of carom seeds"),
            create_ingredient("Mixed Dals", "1 cup", "200g", "One cup of mixed dals for accompanying dal"),
            create_ingredient("Onion", "1 medium", "100g", "One medium onion for dal"),
            create_ingredient("Tomatoes", "2 medium", "200g", "Two medium tomatoes for dal"),
            create_ingredient("Garlic", "4 cloves", "12g", "Four cloves of garlic"),
            create_ingredient("Cumin Seeds", "1 tsp", "5g", "One teaspoon of cumin seeds"),
        ],
        "steps": [
            "Mix wheat flour, semolina, 3 tbsp ghee, ajwain, and salt.",
            "Knead into very stiff dough with water. Rest for 20 minutes.",
            "Shape into round balls, slightly flattened.",
            "Boil baflas in water for 20-25 minutes until they float and are cooked.",
            "Remove, let cool slightly.",
            "Heat remaining ghee, deep fry boiled baflas until golden brown.",
            "Alternatively, bake in oven at 200°C for 20 minutes after boiling.",
            "For dal: Cook mixed dals, prepare tadka with ghee, cumin, onions, tomatoes.",
            "Break hot bafla, soak in ghee.",
            "Serve soaked bafla with dal. Similar to baati but boiled first!",
        ],
    }
def chakki_ki_shaak():
    return {
        "name": "Chakki Ki Shaak",
        "category": "Central India",
        "ingredients": [
            create_ingredient("Wheat Flour", "1 cup", "125g", "One cup of whole wheat flour"),
            create_ingredient("Yogurt", "2 cups", "500g", "Two cups of fresh yogurt"),
            create_ingredient("Gram Flour", "2 tbsp", "20g", "Two tablespoons of gram flour"),
            create_ingredient("Green Chilies", "2", "10g", "Two green chilies, chopped"),
            create_ingredient("Cumin Seeds", "1 tsp", "5g", "One teaspoon of cumin seeds"),
            create_ingredient("Mustard Seeds", "1/2 tsp", "2g", "Half teaspoon of mustard seeds"),
            create_ingredient("Curry Leaves", "10", "5g", "Ten fresh curry leaves"),
            create_ingredient("Ghee", "3 tbsp", "45g", "Three tablespoons of ghee"),
            create_ingredient("Turmeric", "1/4 tsp", "1g", "Quarter teaspoon of turmeric"),
            create_ingredient("Asafoetida", "pinch", "0.5g", "A pinch of asafoetida"),
        ],
        "steps": [
            "Make stiff dough with wheat flour, salt, and water.",
            "Roll small pieces into thin discs (chakkis). Let them dry for 30 minutes.",
            "Whisk yogurt with gram flour, turmeric, and salt until smooth.",
            "Heat ghee, add cumin, mustard seeds. Let splutter.",
            "Add curry leaves, green chilies, asafoetida.",
            "Pour in yogurt mixture, stir continuously.",
            "Cook on low heat, stirring, until it starts to thicken.",
            "Add chakkis (wheat discs) to the yogurt gravy.",
            "Simmer until chakkis are cooked through and gravy coats them.",
            "Serve hot. A unique dish from Malwa region!",
        ],
    }
def mawa_bati():
    return {
        "name": "Mawa Bati",
        "category": "Central India",
        "ingredients": [
            create_ingredient("Khoya (Mawa)", "200g", "200g", "Two hundred grams of fresh khoya, crumbled"),
            create_ingredient("Sugar", "1/2 cup", "100g", "Half cup of sugar"),
            create_ingredient("Cardamom", "4 pods", "2g", "Four green cardamom pods, powdered"),
            create_ingredient("All-Purpose Flour", "1/2 cup", "65g", "Half cup of all-purpose flour"),
            create_ingredient("Ghee", "3 tbsp + for frying", "45g + more", "Three tablespoons ghee in dough, more for frying"),
            create_ingredient("Almonds", "10", "15g", "Ten almonds, slivered"),
            create_ingredient("Pistachios", "10", "10g", "Ten pistachios, slivered"),
            create_ingredient("Saffron", "few strands", "0.2g", "A few strands of saffron"),
            create_ingredient("Rose Water", "1 tsp", "5ml", "One teaspoon of rose water"),
            create_ingredient("Milk", "2 tbsp", "30ml", "Two tablespoons of milk"),
        ],
        "steps": [
            "Crumble khoya and mix with sugar. Cook on low heat until sugar dissolves.",
            "Add cardamom powder, rose water, and saffron soaked in milk.",
            "Cook until mixture thickens and starts to leave the sides of pan.",
            "Remove and let cool enough to handle.",
            "Shape into small round balls (batis).",
            "Decorate tops with almond and pistachio slivers.",
            "Alternatively, coat with flour and deep fry for a different texture.",
            "For fried version: Roll khoya balls in flour, deep fry until golden.",
            "Serve as is or with rabri (sweetened thickened milk).",
            "A rich sweet from the Bundelkhand region!",
        ],
    }
def fara():
    return {
        "name": "Fara",
        "category": "Central India",
        "ingredients": [
            create_ingredient("Rice Flour", "2 cups", "250g", "Two cups of rice flour"),
            create_ingredient("Chana Dal", "1/2 cup", "100g", "Half cup of chana dal, cooked and mashed"),
            create_ingredient("Green Chilies", "2", "10g", "Two green chilies, minced"),
            create_ingredient("Ginger", "1 inch", "10g", "One-inch ginger, grated"),
            create_ingredient("Cumin Seeds", "1 tsp", "5g", "One teaspoon of roasted cumin seeds"),
            create_ingredient("Coriander", "2 tbsp", "10g", "Two tablespoons of fresh coriander"),
            create_ingredient("Mustard Oil", "2 tbsp", "30ml", "Two tablespoons of mustard oil"),
            create_ingredient("Turmeric", "1/4 tsp", "1g", "Quarter teaspoon of turmeric"),
            create_ingredient("Salt", "to taste", "to taste", "Salt adjusted to preference"),
            create_ingredient("Water", "for dough", "for dough", "Hot water for making dough"),
        ],
        "steps": [
            "Boil water, gradually add rice flour, stirring to avoid lumps.",
            "Knead into smooth dough while still warm. Cover with damp cloth.",
            "For filling: Mix mashed dal with green chilies, ginger, cumin, coriander, salt.",
            "Take a portion of dough, flatten into a small disc in palm.",
            "Place filling in center, fold over to make half-moon shape.",
            "Seal edges by pressing with fork or fingers.",
            "Steam faras for 15-20 minutes until cooked through.",
            "Heat mustard oil, temper with cumin and asafoetida.",
            "Drizzle tempered oil over steamed faras.",
            "Serve hot with pickle or chutney. Healthy steamed dumplings from MP!",
        ],
    }

def pani_puri():
    return {
        "name": "Pani Puri",
        "category": "Street Food & Snacks",
        "ingredients": [
            create_ingredient("Semolina", "1 cup", "120g", "One cup of fine semolina (sooji) for puris"),
            create_ingredient("All-Purpose Flour", "2 tbsp", "20g", "Two tablespoons of all-purpose flour"),
            create_ingredient("Mint Leaves", "1 cup", "50g", "One cup of fresh mint leaves for pani"),
            create_ingredient("Coriander Leaves", "1 cup", "50g", "One cup of fresh coriander for pani"),
            create_ingredient("Tamarind", "small ball", "30g", "A small ball of tamarind for sweet chutney"),
            create_ingredient("Boiled Potatoes", "2 medium", "200g", "Two medium boiled potatoes, mashed"),
            create_ingredient("Chickpeas", "1/2 cup", "100g", "Half cup of boiled chickpeas"),
            create_ingredient("Green Chilies", "4", "20g", "Four green chilies"),
            create_ingredient("Cumin Powder", "1 tbsp", "10g", "One tablespoon of roasted cumin powder"),
            create_ingredient("Black Salt", "2 tsp", "10g", "Two teaspoons of black salt for pani"),
        ],
        "steps": [
            "For puris: Mix semolina, flour, salt, a pinch of baking soda. Knead stiff dough. Rest 30 minutes.",
            "Roll thin, cut rounds, prick with fork. Deep fry at high heat until puffed and crispy.",
            "For green pani: Blend mint, coriander, green chilies, ginger, cumin, black salt, with cold water.",
            "Strain and chill. Adjust salt and sourness. Add chilled water to dilute.",
            "For tamarind chutney: Boil tamarind, jaggery, dates. Blend, strain, add spices.",
            "For filling: Mix mashed potato, boiled chickpeas, chaat masala, cumin powder.",
            "Add boondi (optional) to filling mixture.",
            "To serve: Crack top of puri, add potato filling, chickpeas.",
            "Dip in green pani, let it fill.",
            "Eat whole in one bite! Add sweet chutney for variation.",
        ],
    }
def bhel_puri():
    return {
        "name": "Bhel Puri",
        "category": "Street Food & Snacks",
        "ingredients": [
            create_ingredient("Puffed Rice", "4 cups", "100g", "Four cups of puffed rice (murmura)"),
            create_ingredient("Sev", "1 cup", "50g", "One cup of fine sev"),
            create_ingredient("Onion", "1 medium", "100g", "One medium onion, finely chopped"),
            create_ingredient("Tomatoes", "2 medium", "200g", "Two medium tomatoes, finely chopped"),
            create_ingredient("Boiled Potatoes", "2 medium", "200g", "Two medium boiled potatoes, diced"),
            create_ingredient("Green Chutney", "4 tbsp", "60g", "Four tablespoons of mint-coriander chutney"),
            create_ingredient("Tamarind Chutney", "4 tbsp", "60g", "Four tablespoons of sweet tamarind chutney"),
            create_ingredient("Chaat Masala", "1 tsp", "5g", "One teaspoon of chaat masala"),
            create_ingredient("Coriander Leaves", "1/4 cup", "15g", "Quarter cup of chopped coriander"),
            create_ingredient("Green Chilies", "2", "10g", "Two green chilies, chopped"),
        ],
        "steps": [
            "Take puffed rice in a large bowl.",
            "Add chopped onions, tomatoes, boiled potatoes.",
            "Add green chutney and tamarind chutney to taste.",
            "Add chaat masala, salt, red chili powder as desired.",
            "Add chopped green chilies and coriander.",
            "Toss everything together quickly.",
            "Add sev at the very end.",
            "Mix once more and serve immediately.",
            "Must be eaten right away - sev becomes soggy if it sits.",
            "Top with more sev before eating!",
        ],
    }
def sev_puri():
    return {
        "name": "Sev Puri",
        "category": "Street Food & Snacks",
        "ingredients": [
            create_ingredient("Papdi (Flat Puris)", "20 pieces", "100g", "Twenty flat crispy puris (papdi)"),
            create_ingredient("Boiled Potatoes", "2 medium", "200g", "Two medium boiled potatoes, finely diced"),
            create_ingredient("Onion", "1 medium", "100g", "One medium onion, very finely chopped"),
            create_ingredient("Sev", "1 cup", "50g", "One cup of fine crispy sev"),
            create_ingredient("Green Chutney", "1/2 cup", "120g", "Half cup of spicy green chutney"),
            create_ingredient("Tamarind Chutney", "1/2 cup", "120g", "Half cup of sweet tamarind chutney"),
            create_ingredient("Chaat Masala", "1 tsp", "5g", "One teaspoon of chaat masala"),
            create_ingredient("Coriander Leaves", "2 tbsp", "10g", "Two tablespoons of chopped coriander"),
            create_ingredient("Red Chili Powder", "1/2 tsp", "2g", "Half teaspoon of red chili powder"),
            create_ingredient("Salt", "to taste", "to taste", "Salt adjusted to preference"),
        ],
        "steps": [
            "Arrange flat puris (papdis) on a serving plate.",
            "Top each papdi with a little diced potato.",
            "Add finely chopped onions on top.",
            "Drizzle green chutney over each puri.",
            "Add tamarind chutney generously.",
            "Sprinkle chaat masala and red chili powder.",
            "Top liberally with fine sev.",
            "Garnish with chopped coriander.",
            "Serve immediately before puris become soggy.",
            "Each puri should be eaten in one bite for best experience!",
        ],
    }
def kachori():
    return {
        "name": "Kachori",
        "category": "Street Food & Snacks",
        "ingredients": [
            create_ingredient("All-Purpose Flour", "2 cups", "250g", "Two cups of all-purpose flour (maida)"),
            create_ingredient("Moong Dal", "1 cup", "200g", "One cup of split moong dal, soaked"),
            create_ingredient("Fennel Seeds", "1 tsp", "5g", "One teaspoon of fennel seeds"),
            create_ingredient("Coriander Powder", "1 tsp", "5g", "One teaspoon of coriander powder"),
            create_ingredient("Red Chili Powder", "1 tsp", "5g", "One teaspoon of red chili powder"),
            create_ingredient("Ginger", "1 inch", "10g", "One-inch ginger, grated"),
            create_ingredient("Asafoetida", "1/4 tsp", "1g", "Quarter teaspoon of asafoetida"),
            create_ingredient("Ghee", "3 tbsp", "45g", "Three tablespoons of ghee for dough"),
            create_ingredient("Oil", "for frying", "for frying", "Oil for deep frying"),
            create_ingredient("Salt", "to taste", "to taste", "Salt adjusted to preference"),
        ],
        "steps": [
            "Make dough: Mix flour, ghee, salt. Knead with water into stiff dough. Rest 30 minutes.",
            "For filling: Drain soaked dal, grind coarsely.",
            "Heat oil, add asafoetida and fennel seeds.",
            "Add ground dal, ginger, all spices. Cook until mixture is dry, 10-15 minutes.",
            "Let filling cool completely.",
            "Make small balls of dough, flatten into discs.",
            "Place filling in center, gather edges, seal and flatten slightly.",
            "Heat oil to 160°C (325°F) - lower temperature for crispy kachori.",
            "Fry kachoris on medium-low heat until golden on all sides.",
            "Drain and serve hot with tamarind chutney and potato curry.",
        ],
    }


def samosa():
    return {
        "name": "Samosa",
        "category": "Street Food & Snacks",
        "ingredients": [
            create_ingredient("All-Purpose Flour", "2 cups", "250g", "Two cups of all-purpose flour"),
            create_ingredient("Potatoes", "4 large", "500g", "Four large potatoes, boiled and mashed"),
            create_ingredient("Green Peas", "1/2 cup", "75g", "Half cup of green peas"),
            create_ingredient("Cumin Seeds", "1 tsp", "5g", "One teaspoon of cumin seeds"),
            create_ingredient("Coriander Powder", "1 tbsp", "10g", "One tablespoon of coriander powder"),
            create_ingredient("Garam Masala", "1 tsp", "5g", "One teaspoon of garam masala"),
            create_ingredient("Green Chilies", "3", "15g", "Three green chilies, chopped"),
            create_ingredient("Ginger", "1 inch", "10g", "One-inch ginger, grated"),
            create_ingredient("Ghee", "3 tbsp", "45g", "Three tablespoons of ghee for dough"),
            create_ingredient("Oil", "for frying", "for frying", "Oil for deep frying"),
        ],
        "steps": [
            "Make dough: Mix flour, ghee (or oil), carom seeds, salt. Knead stiff dough. Rest 30 minutes.",
            "For filling: Heat oil, add cumin seeds.",
            "Add green chilies, ginger. Sauté briefly.",
            "Add mashed potatoes, peas, all spices. Mix well, cook 5 minutes.",
            "Add coriander leaves. Let cool completely.",
            "Divide dough into balls, roll into ovals.",
            "Cut each oval in half. Form cone by overlapping straight edges, seal with water.",
            "Fill cone with potato mixture, seal top edge.",
            "Heat oil to 160°C (325°F). Fry samosas on medium-low until golden.",
            "Slow frying ensures crispy, flaky layers. Serve with green and tamarind chutney.",
        ],
    }
def pakora():
    return {
        "name": "Pakora",
        "category": "Street Food & Snacks",
        "ingredients": [
            create_ingredient("Gram Flour", "1 cup", "120g", "One cup of gram flour (besan)"),
            create_ingredient("Onions", "2 large", "300g", "Two large onions, thinly sliced"),
            create_ingredient("Spinach", "1 cup", "50g", "One cup of spinach leaves (for palak pakora)"),
            create_ingredient("Potatoes", "2 medium", "200g", "Two medium potatoes, thinly sliced"),
            create_ingredient("Green Chilies", "2", "10g", "Two green chilies, chopped"),
            create_ingredient("Red Chili Powder", "1 tsp", "5g", "One teaspoon of red chili powder"),
            create_ingredient("Carom Seeds", "1/2 tsp", "2g", "Half teaspoon of carom seeds (ajwain)"),
            create_ingredient("Baking Soda", "pinch", "pinch", "A pinch of baking soda for crispness"),
            create_ingredient("Oil", "for frying", "for frying", "Oil for deep frying"),
            create_ingredient("Salt", "to taste", "to taste", "Salt adjusted to preference"),
        ],
        "steps": [
            "Mix gram flour with red chili, carom seeds, baking soda, salt.",
            "Add water gradually to make thick batter that coats vegetables.",
            "For onion pakora: Add sliced onions to batter, mix well.",
            "For palak pakora: Dip whole spinach leaves in batter.",
            "For aloo pakora: Coat potato slices with batter.",
            "Heat oil to 180°C (350°F).",
            "For onion pakora: Drop spoonfuls into hot oil.",
            "For other pakoras: Fry coated vegetables until golden.",
            "Fry until crispy and golden brown on all sides.",
            "Drain on paper. Serve hot with mint chutney. Perfect with chai on rainy days!",
        ],
    }
def dabeli():
    return {
        "name": "Dabeli",
        "category": "Street Food & Snacks",
        "ingredients": [
            create_ingredient("Pav Buns", "8", "8 pieces", "Eight soft pav buns"),
            create_ingredient("Potatoes", "4 medium", "400g", "Four medium potatoes, boiled and mashed"),
            create_ingredient("Dabeli Masala", "3 tbsp", "25g", "Three tablespoons of special dabeli masala"),
            create_ingredient("Tamarind Chutney", "1/2 cup", "120g", "Half cup of sweet tamarind-date chutney"),
            create_ingredient("Garlic Chutney", "1/4 cup", "40g", "Quarter cup of dry red garlic chutney"),
            create_ingredient("Pomegranate Seeds", "1/4 cup", "40g", "Quarter cup of fresh pomegranate seeds"),
            create_ingredient("Roasted Peanuts", "1/4 cup", "40g", "Quarter cup of roasted peanuts, crushed"),
            create_ingredient("Sev", "1/2 cup", "25g", "Half cup of fine sev"),
            create_ingredient("Fresh Coconut", "2 tbsp", "15g", "Two tablespoons of grated fresh coconut"),
            create_ingredient("Coriander", "2 tbsp", "10g", "Two tablespoons of chopped coriander"),
        ],
        "steps": [
            "Mix mashed potatoes with dabeli masala, salt, and 2 tbsp tamarind chutney.",
            "Slit pav buns horizontally without separating.",
            "Apply tamarind chutney on one half, garlic chutney on other.",
            "Place generous portion of potato mixture inside pav.",
            "Add pomegranate seeds, crushed peanuts.",
            "Sprinkle grated coconut and coriander.",
            "Close the pav gently.",
            "Toast on tawa with butter until golden on both sides.",
            "Top with sev and more pomegranate seeds.",
            "Serve hot. Kutchi specialty from Gujarat!",
        ],
    }
def chaat():
    return {
        "name": "Chaat",
        "category": "Street Food & Snacks",
        "ingredients": [
            create_ingredient("Papdi", "20 pieces", "100g", "Twenty crispy flat puris"),
            create_ingredient("Boiled Potatoes", "2 medium", "200g", "Two medium boiled potatoes, cubed"),
            create_ingredient("Chickpeas", "1/2 cup", "100g", "Half cup of boiled chickpeas"),
            create_ingredient("Yogurt", "1 cup", "250g", "One cup of whisked creamy yogurt"),
            create_ingredient("Tamarind Chutney", "1/2 cup", "120g", "Half cup of sweet tamarind chutney"),
            create_ingredient("Green Chutney", "1/2 cup", "120g", "Half cup of mint-coriander chutney"),
            create_ingredient("Chaat Masala", "2 tsp", "10g", "Two teaspoons of chaat masala"),
            create_ingredient("Cumin Powder", "1 tsp", "5g", "One teaspoon of roasted cumin powder"),
            create_ingredient("Sev", "1/2 cup", "25g", "Half cup of fine sev"),
            create_ingredient("Coriander", "2 tbsp", "10g", "Two tablespoons of fresh coriander"),
        ],
        "steps": [
            "Arrange broken papdis on a plate.",
            "Add boiled potato cubes and chickpeas.",
            "Pour whisked yogurt over everything.",
            "Drizzle tamarind chutney generously.",
            "Add green chutney as desired.",
            "Sprinkle chaat masala and roasted cumin.",
            "Add a pinch of red chili powder.",
            "Top with sev and fresh coriander.",
            "Mix gently just before eating if preferred.",
            "Enjoy the mix of sweet, sour, spicy, and crunchy!",
        ],
    }
def egg_roll():
    return {
        "name": "Egg Roll",
        "category": "Street Food & Snacks",
        "ingredients": [
            create_ingredient("All-Purpose Flour", "2 cups", "250g", "Two cups of all-purpose flour for paratha"),
            create_ingredient("Eggs", "4", "4 pieces", "Four large eggs"),
            create_ingredient("Onion", "2 medium", "200g", "Two medium onions, thinly sliced"),
            create_ingredient("Green Chilies", "4", "20g", "Four green chilies, sliced"),
            create_ingredient("Cucumber", "1 small", "100g", "One small cucumber, julienned"),
            create_ingredient("Lime Juice", "2 tbsp", "30ml", "Two tablespoons of fresh lime juice"),
            create_ingredient("Chaat Masala", "1 tsp", "5g", "One teaspoon of chaat masala"),
            create_ingredient("Kasundi", "2 tbsp", "30g", "Two tablespoons of Bengali mustard sauce"),
            create_ingredient("Oil", "for cooking", "for cooking", "Oil for cooking parathas"),
            create_ingredient("Salt", "to taste", "to taste", "Salt adjusted to preference"),
        ],
        "steps": [
            "Make dough: Mix flour, salt, oil, water. Knead soft dough. Rest 20 minutes.",
            "Roll into thin parathas.",
            "Cook paratha on tawa with oil until light golden.",
            "Beat egg with salt, pour over paratha on tawa.",
            "Flip so egg side cooks on tawa.",
            "Cook until egg is set and paratha is crispy.",
            "Place on plate, egg side up.",
            "Add sliced onions, green chilies, cucumber in center.",
            "Sprinkle chaat masala, drizzle lime juice and kasundi.",
            "Roll tightly, wrap in paper. Iconic Kolkata street food!",
        ],
    }
def keema_pav():
    return {
        "name": "Keema Pav",
        "category": "Street Food & Snacks",
        "ingredients": [
            create_ingredient("Mutton Mince", "500g", "500g", "Five hundred grams of mutton or lamb mince"),
            create_ingredient("Onions", "3 large", "450g", "Three large onions, finely chopped"),
            create_ingredient("Tomatoes", "2 medium", "200g", "Two medium tomatoes, chopped"),
            create_ingredient("Ginger-Garlic Paste", "2 tbsp", "30g", "Two tablespoons of ginger-garlic paste"),
            create_ingredient("Pav Buns", "8", "8 pieces", "Eight soft pav buns"),
            create_ingredient("Green Peas", "1/2 cup", "75g", "Half cup of green peas"),
            create_ingredient("Garam Masala", "1 tsp", "5g", "One teaspoon of garam masala"),
            create_ingredient("Cumin Powder", "1 tsp", "5g", "One teaspoon of cumin powder"),
            create_ingredient("Butter", "4 tbsp", "60g", "Four tablespoons of butter"),
            create_ingredient("Coriander", "1/4 cup", "15g", "Quarter cup of fresh coriander"),
        ],
        "steps": [
            "Heat oil, fry onions until deep golden brown.",
            "Add ginger-garlic paste, cook for 2 minutes.",
            "Add tomatoes, cook until soft and oil separates.",
            "Add minced meat, break up any lumps.",
            "Cook on high heat until meat browns, about 10 minutes.",
            "Add cumin, coriander powder, red chili, turmeric, salt.",
            "Add 1/2 cup water, cover and cook until meat is done.",
            "Add green peas, cook until tender.",
            "Add garam masala and fresh coriander.",
            "Slit and butter pav, toast. Serve keema with buttery pav.",
        ],
    }
def gulab_jamun():
    return {
        "name": "Gulab Jamun",
        "category": "Sweets & Desserts",
        "ingredients": [
            create_ingredient("Khoya (Mawa)", "250g", "250g", "Two hundred fifty grams of soft khoya"),
            create_ingredient("All-Purpose Flour", "3 tbsp", "30g", "Three tablespoons of all-purpose flour"),
            create_ingredient("Baking Soda", "pinch", "pinch", "A tiny pinch of baking soda"),
            create_ingredient("Sugar", "2 cups", "400g", "Two cups of sugar for syrup"),
            create_ingredient("Water", "1.5 cups", "375ml", "One and half cups of water for syrup"),
            create_ingredient("Cardamom", "4 pods", "2g", "Four green cardamom pods, crushed"),
            create_ingredient("Rose Water", "1 tbsp", "15ml", "One tablespoon of rose water"),
            create_ingredient("Saffron", "few strands", "0.2g", "A few strands of saffron"),
            create_ingredient("Ghee", "for frying", "for frying", "Ghee for deep frying"),
            create_ingredient("Milk", "1-2 tbsp", "15-30ml", "One to two tablespoons of milk if needed"),
        ],
        "steps": [
            "Make syrup: Boil sugar with water until slightly sticky (one-string consistency).",
            "Add cardamom, saffron, rose water. Keep warm.",
            "Crumble khoya, add flour and baking soda.",
            "Knead gently to form smooth dough. Add milk if dry.",
            "Divide into small equal portions (about 20-25).",
            "Roll into smooth crack-free balls.",
            "Heat ghee on low flame to 130°C (265°F) - temperature is critical!",
            "Fry jamuns on very low heat, turning constantly, until deep brown.",
            "Remove and immediately soak in warm syrup.",
            "Let soak for at least 2 hours. Serve warm or at room temperature.",
        ],
    }
def rasgulla():
    return {
        "name": "Rasgulla",
        "category": "Sweets & Desserts",
        "ingredients": [
            create_ingredient("Milk", "1 liter", "1000ml", "One liter of full-fat milk"),
            create_ingredient("Lemon Juice", "3 tbsp", "45ml", "Three tablespoons of lemon juice or vinegar"),
            create_ingredient("Sugar", "1.5 cups", "300g", "One and half cups of sugar for syrup"),
            create_ingredient("Water", "4 cups", "1 liter", "Four cups of water for syrup"),
            create_ingredient("Cardamom", "2 pods", "1g", "Two green cardamom pods"),
            create_ingredient("Rose Water", "1 tsp", "5ml", "One teaspoon of rose water (optional)"),
            create_ingredient("Ice Cubes", "few", "few", "A few ice cubes to stop cooking of chhena"),
            create_ingredient("Salt", "pinch", "pinch", "A pinch of salt"),
            create_ingredient("Cornstarch", "1 tsp", "3g", "One teaspoon of cornstarch (optional, for smooth texture)"),
            create_ingredient("Semolina", "1/2 tsp", "2g", "Half teaspoon of fine semolina (optional)"),
        ],
        "steps": [
            "Boil milk, add lemon juice gradually while stirring until it curdles completely.",
            "Strain through muslin cloth, rinse chhena under cold water.",
            "Squeeze out all water, chhena should be moist but not wet.",
            "Knead chhena on flat surface for 10-15 minutes until smooth and no grains remain.",
            "Add cornstarch if using, knead more. Divide into equal small balls.",
            "Make syrup: Boil sugar and water in a wide pan.",
            "When syrup boils, gently add chhena balls.",
            "Cover and cook on high heat for 15 minutes. They will double in size.",
            "Check that they're spongy throughout - press gently, they should spring back.",
            "Let cool in syrup. Chill before serving. Authentic Bengali sweet!",
        ],
    }
def sandesh():
    return {
        "name": "Sandesh",
        "category": "Sweets & Desserts",
        "ingredients": [
            create_ingredient("Milk", "1 liter", "1000ml", "One liter of full-fat cow's milk"),
            create_ingredient("Lemon Juice", "2 tbsp", "30ml", "Two tablespoons of lemon juice"),
            create_ingredient("Sugar", "1/2 cup", "100g", "Half cup of powdered sugar"),
            create_ingredient("Cardamom", "2 pods", "1g", "Two green cardamom pods, powdered"),
            create_ingredient("Pistachios", "10", "10g", "Ten pistachios, slivered for garnish"),
            create_ingredient("Saffron", "few strands", "0.2g", "A few saffron strands (optional)"),
            create_ingredient("Rose Water", "1/2 tsp", "2ml", "Half teaspoon of rose water (optional)"),
            create_ingredient("Mango Pulp", "2 tbsp", "30g", "Two tablespoons of mango pulp for variation"),
            create_ingredient("Cocoa Powder", "1 tsp", "5g", "One teaspoon of cocoa for chocolate version"),
            create_ingredient("Salt", "pinch", "pinch", "A tiny pinch of salt"),
        ],
        "steps": [
            "Boil milk, curdle with lemon juice. Strain and rinse chhena.",
            "Squeeze out all water thoroughly - drier chhena is better for sandesh.",
            "Knead chhena until silky smooth, about 10 minutes.",
            "Cook chhena with sugar in non-stick pan on low heat.",
            "Stir continuously until mixture thickens and leaves pan sides.",
            "Add cardamom powder, rose water, saffron.",
            "Remove when it forms a mass but is still soft.",
            "Cool slightly, shape into desired forms using molds.",
            "Garnish with pistachios and saffron strands.",
            "For variations: add mango pulp or cocoa while cooking. Refrigerate to set.",
        ],
    }
def mishti_doi():
    return {
        "name": "Mishti Doi",
        "category": "Sweets & Desserts",
        "ingredients": [
            create_ingredient("Full-Fat Milk", "1 liter", "1000ml", "One liter of full-fat milk"),
            create_ingredient("Jaggery", "1/2 cup", "100g", "Half cup of date palm jaggery (nolen gur) or regular jaggery"),
            create_ingredient("Yogurt Culture", "2 tbsp", "30g", "Two tablespoons of fresh yogurt as starter"),
            create_ingredient("Sugar", "2 tbsp", "25g", "Two tablespoons of sugar (optional)"),
            create_ingredient("Cardamom", "2 pods", "1g", "Two green cardamom pods (optional)"),
            create_ingredient("Saffron", "few strands", "0.2g", "A few saffron strands for color (optional)"),
            create_ingredient("Clay Pots", "6 small", "6 pieces", "Six small clay pots (matkas) for traditional serving"),
            create_ingredient("Pistachios", "for garnish", "5g", "Slivered pistachios for garnish"),
            create_ingredient("Raisins", "for garnish", "5g", "A few raisins for garnish (optional)"),
            create_ingredient("Cream", "2 tbsp", "30ml", "Two tablespoons of cream (optional, for richer texture)"),
        ],
        "steps": [
            "Reduce milk by boiling until it's about 3/4 of original volume.",
            "Melt jaggery separately with a little water, strain to remove impurities.",
            "Add jaggery syrup to reduced milk. The caramelization is key for flavor.",
            "Traditionally, milk is also caramelized slightly for darker color.",
            "Cool milk mixture to lukewarm (about 40°C/104°F).",
            "Add yogurt starter, mix gently.",
            "Pour into clay pots or ceramic bowls.",
            "Cover and keep in warm place for 8-10 hours or overnight.",
            "Once set, refrigerate for at least 4 hours.",
            "Serve chilled. Clay pots give authentic flavor. Best with nolen gur in winter!",
        ],
    }
def kheer():
    return {
        "name": "Kheer",
        "category": "Sweets & Desserts",
        "ingredients": [
            create_ingredient("Full-Fat Milk", "1 liter", "1000ml", "One liter of full-fat milk"),
            create_ingredient("Basmati Rice", "1/4 cup", "50g", "Quarter cup of basmati rice, soaked"),
            create_ingredient("Sugar", "1/2 cup", "100g", "Half cup of sugar"),
            create_ingredient("Cardamom", "4 pods", "2g", "Four green cardamom pods, crushed"),
            create_ingredient("Saffron", "few strands", "0.5g", "A few saffron strands, soaked in warm milk"),
            create_ingredient("Almonds", "10", "15g", "Ten almonds, blanched and slivered"),
            create_ingredient("Pistachios", "10", "10g", "Ten pistachios, slivered"),
            create_ingredient("Raisins", "2 tbsp", "20g", "Two tablespoons of golden raisins"),
            create_ingredient("Ghee", "1 tbsp", "15g", "One tablespoon of ghee"),
            create_ingredient("Rose Water", "1 tsp", "5ml", "One teaspoon of rose water"),
        ],
        "steps": [
            "Soak rice for 30 minutes, drain.",
            "Bring milk to boil in heavy-bottomed pan, stirring frequently.",
            "Add soaked rice, reduce heat to low.",
            "Simmer, stirring often to prevent sticking, for 45-60 minutes.",
            "Rice should be completely soft and milk reduced to half.",
            "In separate pan, fry raisins and nuts in ghee until raisins puff.",
            "Add sugar to kheer when rice is fully cooked. Stir until dissolved.",
            "Add cardamom, saffron with milk, rose water.",
            "Add fried nuts and raisins.",
            "Serve warm, at room temperature, or chilled. Garnish with more nuts.",
        ],
    }
def payasam():
    return {
        "name": "Payasam",
        "category": "Sweets & Desserts",
        "ingredients": [
            create_ingredient("Vermicelli", "1 cup", "100g", "One cup of fine vermicelli (semiya)"),
            create_ingredient("Milk", "1 liter", "1000ml", "One liter of full-fat milk"),
            create_ingredient("Sugar", "3/4 cup", "150g", "Three-quarter cup of sugar"),
            create_ingredient("Ghee", "4 tbsp", "60g", "Four tablespoons of ghee"),
            create_ingredient("Cashews", "15", "25g", "Fifteen cashews"),
            create_ingredient("Raisins", "2 tbsp", "20g", "Two tablespoons of golden raisins"),
            create_ingredient("Cardamom", "4 pods", "2g", "Four green cardamom pods, powdered"),
            create_ingredient("Saffron", "few strands", "0.3g", "A few saffron strands"),
            create_ingredient("Coconut Milk", "1/2 cup", "125ml", "Half cup of coconut milk (for ada pradhaman style)"),
            create_ingredient("Edible Camphor", "tiny pinch", "tiny pinch", "A tiny pinch of edible camphor (optional)"),
        ],
        "steps": [
            "Heat 2 tbsp ghee, roast vermicelli until golden brown. Set aside.",
            "In remaining ghee, fry cashews and raisins until golden. Set aside.",
            "Boil milk, add roasted vermicelli.",
            "Simmer on low heat until vermicelli is completely cooked, about 15 minutes.",
            "Add sugar, stir until dissolved.",
            "Add cardamom powder and saffron.",
            "For richer taste, add coconut milk at the end.",
            "Add fried cashews and raisins.",
            "Serve warm or cold. Traditional in South Indian festivals and weddings.",
            "For ada pradhaman, use rice ada instead of vermicelli.",
        ],
    }
def jalebi():
    return {
        "name": "Jalebi",
        "category": "Sweets & Desserts",
        "ingredients": [
            create_ingredient("All-Purpose Flour", "1 cup", "125g", "One cup of all-purpose flour"),
            create_ingredient("Yogurt", "2 tbsp", "30g", "Two tablespoons of yogurt for fermentation"),
            create_ingredient("Sugar", "2 cups", "400g", "Two cups of sugar for syrup"),
            create_ingredient("Water", "1 cup", "250ml", "One cup of water for syrup"),
            create_ingredient("Saffron", "few strands", "0.3g", "A few saffron strands"),
            create_ingredient("Cardamom", "2 pods", "1g", "Two green cardamom pods"),
            create_ingredient("Ghee", "for frying", "for frying", "Ghee for deep frying"),
            create_ingredient("Citric Acid", "1/4 tsp", "1g", "Quarter teaspoon of citric acid for syrup"),
            create_ingredient("Baking Powder", "1/4 tsp", "1g", "Quarter teaspoon of baking powder (for instant version)"),
            create_ingredient("Yellow Food Color", "pinch", "pinch", "A pinch of yellow-orange food color (optional)"),
        ],
        "steps": [
            "Mix flour, yogurt, and enough water to make thin pouring batter.",
            "Cover and ferment overnight or 8-10 hours. Batter should be bubbly.",
            "For instant: add baking powder and let rest 30 minutes.",
            "Make syrup: Boil sugar, water, saffron, cardamom to one-string consistency.",
            "Add citric acid to prevent crystallization. Keep syrup warm.",
            "Heat ghee to 180°C (350°F).",
            "Pour batter into squeeze bottle or cloth with small hole.",
            "Pipe batter in spiral shapes directly into hot ghee.",
            "Fry until crispy and golden on both sides.",
            "Immediately dip in warm syrup for 30 seconds, remove. Serve hot and crispy!",
        ],
    }
def balushahi():
    return {
        "name": "Balushahi",
        "category": "Sweets & Desserts",
        "ingredients": [
            create_ingredient("All-Purpose Flour", "2 cups", "250g", "Two cups of all-purpose flour"),
            create_ingredient("Ghee", "1/2 cup + for frying", "120g + more", "Half cup ghee for dough, more for frying"),
            create_ingredient("Yogurt", "2 tbsp", "30g", "Two tablespoons of thick yogurt"),
            create_ingredient("Baking Soda", "1/4 tsp", "1g", "Quarter teaspoon of baking soda"),
            create_ingredient("Sugar", "2 cups", "400g", "Two cups of sugar for syrup"),
            create_ingredient("Water", "1 cup", "250ml", "One cup of water for syrup"),
            create_ingredient("Cardamom", "4 pods", "2g", "Four green cardamom pods, crushed"),
            create_ingredient("Rose Water", "1 tsp", "5ml", "One teaspoon of rose water"),
            create_ingredient("Saffron", "few strands", "0.2g", "A few saffron strands"),
            create_ingredient("Pistachios", "for garnish", "10g", "Crushed pistachios for garnish"),
        ],
        "steps": [
            "Rub ghee into flour until mixture resembles breadcrumbs.",
            "Add yogurt, baking soda, mix gently. Do not overwork.",
            "Add water sparingly to form soft but stiff dough.",
            "Let dough rest for 20 minutes covered.",
            "Make sugar syrup with one-string consistency, add cardamom, saffron.",
            "Divide dough into equal balls, flatten slightly, make dent in center.",
            "Heat ghee on medium-low heat (150°C/300°F).",
            "Fry balushahis on very low heat for 15-20 minutes until golden throughout.",
            "They should be crispy outside, flaky and soft inside.",
            "Soak in warm syrup for 10 minutes. Garnish with pistachios.",
        ],
    }
def modak():
    return {
        "name": "Modak",
        "category": "Sweets & Desserts",
        "ingredients": [
            create_ingredient("Rice Flour", "1 cup", "125g", "One cup of fine rice flour"),
            create_ingredient("Fresh Coconut", "1 cup", "100g", "One cup of freshly grated coconut"),
            create_ingredient("Jaggery", "3/4 cup", "150g", "Three-quarter cup of grated jaggery"),
            create_ingredient("Cardamom", "4 pods", "2g", "Four green cardamom pods, powdered"),
            create_ingredient("Ghee", "2 tbsp", "30g", "Two tablespoons of ghee"),
            create_ingredient("Poppy Seeds", "1 tbsp", "10g", "One tablespoon of poppy seeds (optional)"),
            create_ingredient("Salt", "pinch", "pinch", "A pinch of salt"),
            create_ingredient("Water", "1 cup", "250ml", "One cup of water for dough"),
            create_ingredient("Nutmeg", "pinch", "pinch", "A pinch of grated nutmeg"),
            create_ingredient("Raisins", "1 tbsp", "10g", "One tablespoon of chopped raisins (optional)"),
        ],
        "steps": [
            "For filling: Heat ghee, add coconut and jaggery. Cook until jaggery melts.",
            "Add cardamom, poppy seeds, nutmeg. Cook until mixture comes together.",
            "Let filling cool. Divide into small portions.",
            "For dough: Boil water with salt and 1 tsp ghee.",
            "Add rice flour all at once, stir vigorously to avoid lumps.",
            "Cover and let steam for 2 minutes.",
            "Knead while warm to smooth, pliable dough. Keep covered.",
            "Take a portion, shape into cup, place filling, close and shape into pleats.",
            "Traditional shape has pointed top with pleated sides.",
            "Steam modaks for 10-12 minutes. Serve warm. Lord Ganesha's favorite!",
        ],
    }
def peda():
    return {
        "name": "Peda",
        "category": "Sweets & Desserts",
        "ingredients": [
            create_ingredient("Khoya (Mawa)", "250g", "250g", "Two hundred fifty grams of fresh khoya"),
            create_ingredient("Sugar", "1/2 cup", "100g", "Half cup of powdered sugar"),
            create_ingredient("Cardamom", "4 pods", "2g", "Four green cardamom pods, powdered"),
            create_ingredient("Saffron", "few strands", "0.3g", "A few saffron strands"),
            create_ingredient("Pistachios", "10", "10g", "Ten pistachios, slivered"),
            create_ingredient("Almonds", "8", "10g", "Eight almonds, slivered"),
            create_ingredient("Ghee", "1 tbsp", "15g", "One tablespoon of ghee"),
            create_ingredient("Milk", "1 tbsp", "15ml", "One tablespoon of milk (if needed)"),
            create_ingredient("Rose Water", "1/2 tsp", "2ml", "Half teaspoon of rose water (optional)"),
            create_ingredient("Nutmeg", "pinch", "pinch", "A pinch of grated nutmeg"),
        ],
        "steps": [
            "Crumble khoya into small pieces.",
            "Heat in heavy-bottomed pan on low flame, stirring constantly.",
            "Cook until khoya softens and fat begins to separate, about 5 minutes.",
            "Add powdered sugar, continue stirring.",
            "Cook until mixture thickens and starts leaving the sides.",
            "Add cardamom, saffron, nutmeg, rose water.",
            "Remove from heat when it forms a mass but is still soft.",
            "Cool until warm enough to handle.",
            "Shape into round flattened discs or use molds.",
            "Press a pistachio or almond sliver on top. Classic Mathura peda!",
        ],
    }
def lucknowi_biryani():
    return {
        "name": "Lucknowi Biryani",
        "category": "Biryani & Rice Varieties",
        "ingredients": [
            create_ingredient("Basmati Rice", "2 cups", "400g", "Two cups of aged basmati rice, soaked"),
            create_ingredient("Lamb", "750g", "750g", "Seven hundred fifty grams of lamb pieces"),
            create_ingredient("Yogurt", "1 cup", "250g", "One cup of whisked yogurt"),
            create_ingredient("Onions", "4 large", "600g", "Four large onions, thinly sliced"),
            create_ingredient("Ghee", "1/2 cup", "120g", "Half cup of pure ghee"),
            create_ingredient("Saffron", "1/4 tsp", "0.5g", "Quarter teaspoon of saffron in warm milk"),
            create_ingredient("Rose Water", "2 tbsp", "30ml", "Two tablespoons of rose water"),
            create_ingredient("Kewra Water", "1 tbsp", "15ml", "One tablespoon of kewra (screwpine) essence"),
            create_ingredient("Lucknowi Biryani Masala", "2 tbsp", "20g", "Two tablespoons of Lucknowi spice blend"),
            create_ingredient("Mint & Coriander", "1 cup each", "100g", "One cup each of fresh mint and coriander"),
        ],
        "steps": [
            "Marinate lamb with yogurt, ginger-garlic paste, biryani masala, salt for 4 hours.",
            "Fry onions in ghee until deep golden (birista). Reserve half for layering.",
            "Cook marinated lamb with remaining onions until 80% done.",
            "Parboil rice with whole spices until 70% cooked.",
            "In heavy pot, layer: meat, then rice, then fried onions, mint, coriander.",
            "Sprinkle saffron milk, rose water, kewra, and dots of ghee.",
            "Repeat layers. Top with rice.",
            "Seal with dough. First cook on high heat for 5 minutes.",
            "Then reduce to lowest heat for 40 minutes (dum).",
            "Lucknowi style is more fragrant, less spicy than Hyderabadi. Serve with korma.",
        ],
    }
def kolkata_biryani():
    return {
        "name": "Kolkata Biryani",
        "category": "Biryani & Rice Varieties",
        "ingredients": [
            create_ingredient("Basmati Rice", "2 cups", "400g", "Two cups of aged basmati rice"),
            create_ingredient("Mutton", "600g", "600g", "Six hundred grams of mutton pieces"),
            create_ingredient("Potatoes", "4 medium", "400g", "Four medium potatoes, peeled and halved"),
            create_ingredient("Eggs", "4", "4 pieces", "Four hard-boiled eggs"),
            create_ingredient("Yogurt", "1 cup", "250g", "One cup of thick yogurt"),
            create_ingredient("Ghee", "1/2 cup", "120g", "Half cup of ghee"),
            create_ingredient("Saffron", "1/4 tsp", "0.5g", "Quarter teaspoon of saffron"),
            create_ingredient("Rose Water", "1 tbsp", "15ml", "One tablespoon of rose water"),
            create_ingredient("Nutmeg-Mace", "1/4 tsp each", "1g", "Quarter teaspoon each of nutmeg and mace"),
            create_ingredient("Onions", "4 large", "600g", "Four large onions, sliced thin"),
        ],
        "steps": [
            "The potato is the signature of Kolkata biryani, introduced by Wajid Ali Shah.",
            "Marinate mutton with yogurt, ginger-garlic paste, spices, nutmeg, mace.",
            "Fry onions until deep brown. Reserve half.",
            "Fry potato halves until golden. Set aside.",
            "Cook marinated meat with remaining onions until tender.",
            "Parboil rice with whole spices until 70% done.",
            "Layer in pot: meat, potatoes, rice, fried onions, saffron milk.",
            "Add rose water and ghee.",
            "Seal and cook on dum for 40 minutes.",
            "Serve with potatoes and boiled eggs. The potato absorbs all the flavors!",
        ],
    }
def ambur_biryani():
    return {
        "name": "Ambur Biryani",
        "category": "Biryani & Rice Varieties",
        "ingredients": [
            create_ingredient("Seeraga Samba Rice", "2 cups", "400g", "Two cups of seeraga samba (jeera) rice"),
            create_ingredient("Chicken", "750g", "750g", "Seven hundred fifty grams of chicken pieces"),
            create_ingredient("Yogurt", "1/2 cup", "125g", "Half cup of thick curd"),
            create_ingredient("Onions", "3 large", "450g", "Three large onions, sliced"),
            create_ingredient("Mint Leaves", "1 cup", "50g", "One cup of fresh mint leaves"),
            create_ingredient("Coriander Leaves", "1 cup", "50g", "One cup of fresh coriander"),
            create_ingredient("Green Chilies", "6", "30g", "Six green chilies"),
            create_ingredient("Ginger-Garlic Paste", "2 tbsp", "30g", "Two tablespoons of ginger-garlic paste"),
            create_ingredient("Oil", "4 tbsp", "60ml", "Four tablespoons of oil"),
            create_ingredient("Lime", "1", "1 piece", "One lime, juiced"),
        ],
        "steps": [
            "Ambur biryani uses seeraga samba rice - smaller grains, more flavor.",
            "Marinate chicken with yogurt, ginger-garlic paste, spices, lime juice.",
            "Soak rice for 30 minutes, drain.",
            "Fry onions until golden. Add marinated chicken.",
            "Cook until chicken is half done.",
            "Add mint, coriander, green chilies.",
            "Add soaked rice on top of chicken. Do not mix.",
            "Add water (1.5 times of rice), salt.",
            "Cover and cook on low heat until rice is done.",
            "Traditionally served with dalcha (spicy dal) and brinjal curry.",
        ],
    }
def dindigul_biryani():
    return {
        "name": "Dindigul Biryani",
        "category": "Biryani & Rice Varieties",
        "ingredients": [
            create_ingredient("Seeraga Samba Rice", "2 cups", "400g", "Two cups of seeraga samba rice"),
            create_ingredient("Mutton", "500g", "500g", "Five hundred grams of mutton with small bones"),
            create_ingredient("Coconut Milk", "1/2 cup", "125ml", "Half cup of thin coconut milk"),
            create_ingredient("Yogurt", "1/4 cup", "60g", "Quarter cup of sour curd"),
            create_ingredient("Onions", "3 large", "450g", "Three large onions, sliced"),
            create_ingredient("Tomatoes", "2 medium", "200g", "Two medium tomatoes, chopped"),
            create_ingredient("Mint Leaves", "1/2 cup", "25g", "Half cup of fresh mint"),
            create_ingredient("Fennel Seeds", "1 tbsp", "10g", "One tablespoon of fennel seeds"),
            create_ingredient("Star Anise", "2", "2g", "Two whole star anise"),
            create_ingredient("Oil", "4 tbsp", "60ml", "Four tablespoons of oil"),
        ],
        "steps": [
            "Dindigul biryani is known for small meat pieces and peppery flavor.",
            "Cut mutton into small cube pieces.",
            "Fry onions until brown. Add tomatoes, cook until soft.",
            "Add mutton, all spices including generous pepper. Brown well.",
            "Add yogurt, cook until oil separates.",
            "Add coconut milk and water. Cook mutton until tender.",
            "Add soaked rice on top. Do not stir.",
            "Add mint leaves. Cover tightly.",
            "Cook on low heat until rice is done and meat is tender.",
            "Known for its peppery taste. Serve with raita and salna.",
        ],
    }
def thalassery_biryani():
    return {
        "name": "Thalassery Biryani",
        "category": "Biryani & Rice Varieties",
        "ingredients": [
            create_ingredient("Kaima/Jeerakasala Rice", "2 cups", "400g", "Two cups of kaima or jeerakasala rice"),
            create_ingredient("Chicken", "750g", "750g", "Seven hundred fifty grams of chicken"),
            create_ingredient("Onions", "4 large", "600g", "Four large onions, thinly sliced"),
            create_ingredient("Cashews", "20", "40g", "Twenty whole cashews"),
            create_ingredient("Raisins", "2 tbsp", "20g", "Two tablespoons of golden raisins"),
            create_ingredient("Ghee", "1/2 cup", "120g", "Half cup of ghee"),
            create_ingredient("Coconut Milk", "1 cup", "250ml", "One cup of thick coconut milk"),
            create_ingredient("Garam Masala", "1 tbsp", "10g", "One tablespoon of Malabar garam masala"),
            create_ingredient("Tomatoes", "2 medium", "200g", "Two medium tomatoes"),
            create_ingredient("Mint", "1/2 cup", "25g", "Half cup of fresh mint"),
        ],
        "steps": [
            "This Malabar biryani uses short-grain kaima rice, cooked separately.",
            "Cook rice with whole spices until just done. Spread to cool.",
            "Fry onions until very crispy (birista). Remove most, keep some in pan.",
            "Fry cashews and raisins in ghee. Set aside.",
            "Cook chicken with remaining onions, spices, tomatoes until done.",
            "Add coconut milk, simmer until gravy thickens.",
            "In large pot, layer rice and chicken alternately.",
            "Top with fried onions, cashews, raisins, mint.",
            "Drizzle ghee, cover with tight lid.",
            "Dum for 20 minutes on low heat. The rice stays separate. Malabar specialty!",
        ],
    }
def bamboo_biryani():
    return {
        "name": "Bamboo Biryani",
        "category": "Biryani & Rice Varieties",
        "ingredients": [
            create_ingredient("Basmati Rice", "1.5 cups", "300g", "One and half cups of basmati rice"),
            create_ingredient("Chicken", "400g", "400g", "Four hundred grams of boneless chicken"),
            create_ingredient("Bamboo Tube", "2", "2 pieces", "Two fresh bamboo tubes (hollow)"),
            create_ingredient("Coconut Milk", "1/2 cup", "125ml", "Half cup of coconut milk"),
            create_ingredient("Onions", "2 large", "300g", "Two large onions, sliced"),
            create_ingredient("Ginger-Garlic Paste", "1 tbsp", "15g", "One tablespoon of ginger-garlic paste"),
            create_ingredient("Biryani Masala", "2 tbsp", "20g", "Two tablespoons of biryani masala"),
            create_ingredient("Mint Leaves", "1/2 cup", "25g", "Half cup of fresh mint"),
            create_ingredient("Ghee", "3 tbsp", "45g", "Three tablespoons of ghee"),
            create_ingredient("Saffron", "few strands", "0.3g", "A few saffron strands"),
        ],
        "steps": [
            "Cut fresh bamboo into tube sections, keeping one end sealed naturally.",
            "Marinate chicken with yogurt, biryani masala, ginger-garlic paste.",
            "Fry onions until golden, add marinated chicken, cook partially.",
            "Parboil rice until 70% done.",
            "Layer inside bamboo tube: chicken at bottom, then rice, mint, saffron.",
            "Add coconut milk and ghee.",
            "Seal open end with banana leaf or foil.",
            "Roast bamboo over charcoal fire, rotating regularly, for 30-40 minutes.",
            "The bamboo imparts a unique smoky, earthy flavor.",
            "Cut bamboo to serve. Specialty of Agumbe, Karnataka.",
        ],
    }
def jeera_rice():
    return {
        "name": "Jeera Rice",
        "category": "Biryani & Rice Varieties",
        "ingredients": [
            create_ingredient("Basmati Rice", "1.5 cups", "300g", "One and half cups of basmati rice"),
            create_ingredient("Cumin Seeds", "1.5 tbsp", "12g", "One and half tablespoons of whole cumin seeds"),
            create_ingredient("Ghee", "3 tbsp", "45g", "Three tablespoons of ghee"),
            create_ingredient("Bay Leaves", "2", "2g", "Two bay leaves"),
            create_ingredient("Cloves", "4", "1g", "Four whole cloves"),
            create_ingredient("Green Cardamom", "3 pods", "1.5g", "Three green cardamom pods"),
            create_ingredient("Water", "3 cups", "750ml", "Three cups of water"),
            create_ingredient("Salt", "1 tsp", "6g", "One teaspoon of salt"),
            create_ingredient("Cinnamon", "1 inch", "2g", "One-inch cinnamon stick"),
            create_ingredient("Fresh Coriander", "2 tbsp", "10g", "Two tablespoons for garnish"),
        ],
        "steps": [
            "Wash and soak basmati rice for 30 minutes. Drain well.",
            "Heat ghee in heavy-bottomed pot.",
            "Add cumin seeds, let them sizzle and turn aromatic.",
            "Add bay leaves, cloves, cardamom, cinnamon.",
            "Add drained rice, sauté gently for 2 minutes.",
            "Add water and salt, bring to boil.",
            "Reduce heat to lowest, cover with tight lid.",
            "Cook for 15 minutes without opening lid.",
            "Turn off heat, let rest for 5 minutes.",
            "Fluff gently with fork. Garnish with coriander. Perfect with dal!",
        ],
    }
def curd_rice():
    return {
        "name": "Curd Rice",
        "category": "Biryani & Rice Varieties",
        "ingredients": [
            create_ingredient("Rice", "1 cup", "200g", "One cup of short-grain or parboiled rice"),
            create_ingredient("Curd (Yogurt)", "2 cups", "500g", "Two cups of fresh thick curd"),
            create_ingredient("Milk", "1/2 cup", "125ml", "Half cup of cold milk"),
            create_ingredient("Mustard Seeds", "1 tsp", "5g", "One teaspoon of mustard seeds"),
            create_ingredient("Urad Dal", "1 tsp", "5g", "One teaspoon of split urad dal"),
            create_ingredient("Curry Leaves", "10", "5g", "Ten fresh curry leaves"),
            create_ingredient("Green Chilies", "2", "10g", "Two green chilies, slit"),
            create_ingredient("Ginger", "1 inch", "10g", "One-inch ginger, finely chopped"),
            create_ingredient("Pomegranate Seeds", "2 tbsp", "20g", "Two tablespoons of pomegranate seeds"),
            create_ingredient("Oil", "2 tbsp", "30ml", "Two tablespoons of oil"),
        ],
        "steps": [
            "Cook rice until very soft, slightly overcooked. Let cool.",
            "Mash rice slightly with back of ladle.",
            "Add curd and milk, mix well. Adjust consistency.",
            "Add salt to taste.",
            "Heat oil, add mustard seeds, let splutter.",
            "Add urad dal, fry until golden.",
            "Add curry leaves, green chilies, ginger, asafoetida.",
            "Pour tempering over curd rice, mix well.",
            "Garnish with pomegranate seeds and coriander.",
            "Serve chilled. Best comfort food for hot days!",
        ],
    }
def pulav():
    return {
        "name": "Pulav",
        "category": "Biryani & Rice Varieties",
        "ingredients": [
            create_ingredient("Basmati Rice", "1.5 cups", "300g", "One and half cups of basmati rice"),
            create_ingredient("Mixed Vegetables", "2 cups", "300g", "Two cups of mixed vegetables (peas, carrots, beans, cauliflower)"),
            create_ingredient("Onion", "1 large", "150g", "One large onion, sliced"),
            create_ingredient("Ghee", "3 tbsp", "45g", "Three tablespoons of ghee"),
            create_ingredient("Bay Leaves", "2", "2g", "Two bay leaves"),
            create_ingredient("Cinnamon", "2 inch", "5g", "Two-inch cinnamon stick"),
            create_ingredient("Cardamom", "4 pods", "2g", "Four green cardamom pods"),
            create_ingredient("Cloves", "4", "1g", "Four whole cloves"),
            create_ingredient("Ginger-Garlic Paste", "1 tbsp", "15g", "One tablespoon of ginger-garlic paste"),
            create_ingredient("Mint Leaves", "1/4 cup", "12g", "Quarter cup of fresh mint"),
        ],
        "steps": [
            "Wash and soak rice for 30 minutes. Drain.",
            "Heat ghee, add whole spices (bay leaf, cinnamon, cardamom, cloves).",
            "Add sliced onions, fry until light golden.",
            "Add ginger-garlic paste, sauté for 1 minute.",
            "Add vegetables, sauté for 3-4 minutes.",
            "Add drained rice, gently mix to coat with ghee.",
            "Add water (1.5 times rice), salt, and mint leaves.",
            "Bring to boil, then reduce heat to lowest.",
            "Cover tightly, cook for 15 minutes.",
            "Rest for 5 minutes, fluff gently. Serve with raita.",
        ],
    }
def khichdi():
    return {
        "name": "Khichdi",
        "category": "Biryani & Rice Varieties",
        "ingredients": [
            create_ingredient("Rice", "1 cup", "200g", "One cup of rice"),
            create_ingredient("Moong Dal", "1/2 cup", "100g", "Half cup of split yellow moong dal"),
            create_ingredient("Ghee", "4 tbsp", "60g", "Four tablespoons of ghee"),
            create_ingredient("Cumin Seeds", "1 tsp", "5g", "One teaspoon of cumin seeds"),
            create_ingredient("Turmeric", "1/2 tsp", "2g", "Half teaspoon of turmeric"),
            create_ingredient("Ginger", "1 inch", "10g", "One-inch ginger, grated"),
            create_ingredient("Green Chilies", "2", "10g", "Two green chilies (optional)"),
            create_ingredient("Asafoetida", "pinch", "0.5g", "A pinch of asafoetida"),
            create_ingredient("Salt", "to taste", "to taste", "Salt adjusted to preference"),
            create_ingredient("Water", "4 cups", "1 liter", "Four cups of water"),
        ],
        "steps": [
            "Wash rice and dal together until water runs clear.",
            "Soak together for 20 minutes (optional for softer khichdi).",
            "Heat 2 tbsp ghee in pressure cooker, add cumin seeds.",
            "Add asafoetida, ginger, green chilies. Sauté briefly.",
            "Add drained rice and dal, turmeric, salt.",
            "Add water, mix well.",
            "Pressure cook for 3-4 whistles on medium heat.",
            "Let pressure release naturally.",
            "Khichdi should be soft and porridge-like.",
            "Serve hot with remaining ghee on top, papad, pickle, and kadhi!",
        ],
    }
RECIPES = [
    butter_chicken(),
    dal_makhani(),
    rogan_josh(),
    chole_bhature(),
    paneer_tikka(),
    aloo_paratha(),
    rajma_chawal(),
    kadhi_pakora(),
    tandoori_chicken(),
    nihari(),
    pav_bhaji(),
    vada_pav(),
    misal_pav(),
    goan_fish_curry(),
    sorpotel(),
    undhiyu(),
    dhokla(),
    thepla(),
    laal_maas(),
    dal_baati_churma(),
    masala_dosa(),
    idli_sambar(),
    vada(),
    chettinad_chicken(),
    hyderabadi_biryani(),
    pesarattu(),
    appam_with_stew(),
    kerala_sadya(),
    puliyodarai(),
    rasam(),
    macher_jhol(),
    shorshe_ilish(),
    chingri_malai_curry(),
    pakhala_bhata(),
    dalma(),
    litti_chokha(),
    ghugni(),
    momos(),
    thukpa(),
    sel_roti(),
    poha(),
    bhutte_ka_kees(),
    sabudana_khichdi(),
    indori_sev(),
    dal_pithi(),
    khopra_patties(),
    bafla(),
    chakki_ki_shaak(),
    mawa_bati(),
    fara(),
    pani_puri(),
    bhel_puri(),
    sev_puri(),
    kachori(),
    samosa(),
    pakora(),
    dabeli(),
    chaat(),
    egg_roll(),
    keema_pav(),
    gulab_jamun(),
    rasgulla(),
    sandesh(),
    mishti_doi(),
    kheer(),
    payasam(),
    jalebi(),
    balushahi(),
    modak(),
    peda(),
    lucknowi_biryani(),
    kolkata_biryani(),
    ambur_biryani(),
    dindigul_biryani(),
    thalassery_biryani(),
    bamboo_biryani(),
    jeera_rice(),
    curd_rice(),
    pulav(),
    khichdi(),
]



def get_recipe_color(recipe):
    all_ingredients_lower = " ".join([ing["name"].lower() for ing in recipe["ingredients"]])
    for keyword in NON_VEG_KEYWORDS:
        if keyword in all_ingredients_lower:
            return Colors.RED
    for keyword in DAIRY_KEYWORDS:
        if keyword in all_ingredients_lower:
            return Colors.BLUE
    return Colors.GREEN


def display_header():
    print("\n" + "=" * 60)
    print(f"{Colors.YELLOW}{Colors.BOLD}        🍛  INDIAN RECIPE COOKBOOK  🍛{Colors.RESET}")
    print("=" * 60)
    print(f"{Colors.CYAN}Your guide to authentic Indian cuisine{Colors.RESET}")
    print("-" * 60)


def display_menu():
    print(f"\n{Colors.BOLD}MAIN MENU{Colors.RESET}")
    print("-" * 30)
    print(f"  {Colors.YELLOW}1.{Colors.RESET} List All Recipes")
    print(f"  {Colors.YELLOW}2.{Colors.RESET} View Recipe by Number")
    print(f"  {Colors.YELLOW}3.{Colors.RESET} Search by Ingredient")
    print(f"  {Colors.YELLOW}4.{Colors.RESET} Change Measurement Mode")
    print(f"  {Colors.YELLOW}5.{Colors.RESET} Exit")
    print("-" * 30)


def display_measurement_info():
    global current_measurement_mode
    mode_display = {
        SIMPLE: "Simple (cups/spoons)",
        STANDARD: "Standard (grams/ml)",
        DETAILED: "Detailed (chef-style)",
    }
    print(f"\n{Colors.MAGENTA}Current Measurement Mode: {mode_display[current_measurement_mode]}{Colors.RESET}")


def display_color_legend():
    print(f"\n{Colors.BOLD}Color Guide:{Colors.RESET}")
    print(f"  {Colors.RED}●{Colors.RESET} Non-Vegetarian  {Colors.BLUE}●{Colors.RESET} Dairy-Based  {Colors.GREEN}●{Colors.RESET} Vegetarian")


def list_recipes():
    print(f"\n{Colors.BOLD}{Colors.CYAN}═══════════════════════════════════════════════════════════{Colors.RESET}")
    print(f"{Colors.BOLD}{Colors.CYAN}                    ALL RECIPES ({len(RECIPES)} dishes){Colors.RESET}")
    print(f"{Colors.BOLD}{Colors.CYAN}═══════════════════════════════════════════════════════════{Colors.RESET}")

    display_color_legend()

    categories = {}
    for idx, recipe in enumerate(RECIPES, 1):
        cat = recipe["category"]
        if cat not in categories:
            categories[cat] = []
        categories[cat].append((idx, recipe))

    category_icons = {
        "North India": "🍛",
        "West India": "🌶️",
        "South India": "🥘",
        "East India": "🍲",
        "Central India": "🥗",
        "Street Food & Snacks": "🍴",
        "Sweets & Desserts": "🍮",
        "Biryani & Rice Varieties": "🥘",
    }

    for category, recipe_list in categories.items():
        icon = category_icons.get(category, "🍽️")
        print(f"\n{Colors.YELLOW}{Colors.BOLD}{icon} {category.upper()}{Colors.RESET}")
        print("-" * 50)

        items_per_row = 2
        for i in range(0, len(recipe_list), items_per_row):
            row_items = recipe_list[i:i + items_per_row]
            row_text = ""
            for idx, recipe in row_items:
                color = get_recipe_color(recipe)
                name = recipe["name"][:22]
                row_text += f"  {Colors.WHITE}{idx:2}.{Colors.RESET} {color}{name:<22}{Colors.RESET}"
            print(row_text)

    print(f"\n{Colors.CYAN}{'─' * 60}{Colors.RESET}")


def get_ingredient_display(ingredient):
    global current_measurement_mode
    return f"{ingredient[current_measurement_mode]} {ingredient['name']}"


def show_recipe(recipe_num):
    if recipe_num < 1 or recipe_num > len(RECIPES):
        print(f"\n{Colors.RED}Invalid recipe number. Please enter a number between 1 and {len(RECIPES)}.{Colors.RESET}")
        return

    recipe = RECIPES[recipe_num - 1]
    color = get_recipe_color(recipe)

    print(f"\n{Colors.BOLD}{'═' * 60}{Colors.RESET}")
    print(f"{color}{Colors.BOLD}  {recipe['name'].upper()}{Colors.RESET}")
    print(f"  {Colors.CYAN}Category: {recipe['category']}{Colors.RESET}")
    print(f"{'═' * 60}")

    if color == Colors.RED:
        diet = "🔴 Non-Vegetarian"
    elif color == Colors.BLUE:
        diet = "🔵 Dairy-Based"
    else:
        diet = "🟢 Vegetarian"
    print(f"  {diet}")

    display_measurement_info()

    print(f"\n{Colors.YELLOW}{Colors.BOLD}📝 INGREDIENTS{Colors.RESET}")
    print("-" * 40)
    for ing in recipe["ingredients"]:
        display = get_ingredient_display(ing)
        print(f"  • {display}")

    print(f"\n{Colors.YELLOW}{Colors.BOLD}👨🍳 COOKING STEPS{Colors.RESET}")
    print("-" * 40)
    for i, step in enumerate(recipe["steps"], 1):
        print(f"\n  {Colors.CYAN}Step {i}:{Colors.RESET}")
        words = step.split()
        line = "    "
        for word in words:
            if len(line) + len(word) > 58:
                print(line)
                line = "    " + word + " "
            else:
                line += word + " "
        if line.strip():
            print(line)

    print(f"\n{'─' * 60}")
    print(f"{Colors.GREEN}Enjoy your meal! 🍽️{Colors.RESET}")


def search_ingredient(ingredient):
    ingredient_lower = ingredient.lower().strip()
    if not ingredient_lower:
        print(f"\n{Colors.RED}Please enter a valid ingredient name.{Colors.RESET}")
        return

    found_recipes = []
    for idx, recipe in enumerate(RECIPES, 1):
        for ing in recipe["ingredients"]:
            if ingredient_lower in ing["name"].lower():
                found_recipes.append((idx, recipe))
                break

    if not found_recipes:
        print(f"\n{Colors.RED}No recipes found containing '{ingredient}'.{Colors.RESET}")
        print(f"{Colors.YELLOW}Try searching for common ingredients like: chicken, paneer, rice, potato, etc.{Colors.RESET}")
        return

    print(f"\n{Colors.BOLD}{Colors.CYAN}═══════════════════════════════════════════════════════════{Colors.RESET}")
    print(f"{Colors.BOLD}Found {len(found_recipes)} recipe(s) with '{ingredient}':{Colors.RESET}")
    print(f"{Colors.CYAN}═══════════════════════════════════════════════════════════{Colors.RESET}")

    display_color_legend()
    print()

    for idx, recipe in found_recipes:
        color = get_recipe_color(recipe)
        print(f"  {Colors.WHITE}{idx:2}.{Colors.RESET} {color}{recipe['name']}{Colors.RESET} ({recipe['category']})")

    print(f"\n{Colors.CYAN}{'─' * 60}{Colors.RESET}")


def set_measurement():
    global current_measurement_mode

    print(f"\n{Colors.BOLD}{Colors.YELLOW}MEASUREMENT MODES{Colors.RESET}")
    print("-" * 40)
    print(f"  {Colors.CYAN}1.{Colors.RESET} Simple    - Cups and spoons (e.g., '2 cups')")
    print(f"  {Colors.CYAN}2.{Colors.RESET} Standard  - Grams and ml (e.g., '200g')")
    print(f"  {Colors.CYAN}3.{Colors.RESET} Detailed  - Chef descriptions (full details)")
    print("-" * 40)

    current = {SIMPLE: "1", STANDARD: "2", DETAILED: "3"}
    print(f"{Colors.MAGENTA}Currently selected: Mode {current[current_measurement_mode]}{Colors.RESET}")

    try:
        choice = input(f"\n{Colors.WHITE}Enter mode number (1-3): {Colors.RESET}").strip()
        if choice == "1":
            current_measurement_mode = SIMPLE
            print(f"\n{Colors.GREEN}✓ Switched to Simple mode (cups/spoons){Colors.RESET}")
        elif choice == "2":
            current_measurement_mode = STANDARD
            print(f"\n{Colors.GREEN}✓ Switched to Standard mode (grams/ml){Colors.RESET}")
        elif choice == "3":
            current_measurement_mode = DETAILED
            print(f"\n{Colors.GREEN}✓ Switched to Detailed mode (chef-style){Colors.RESET}")
        else:
            print(f"\n{Colors.RED}Invalid choice. Mode unchanged.{Colors.RESET}")
    except ValueError:
        print(f"\n{Colors.RED}Invalid input. Please enter a number.{Colors.RESET}")


def main():
    display_header()
    display_color_legend()
    display_measurement_info()

    while True:
        display_menu()
        try:
            choice = input(f"\n{Colors.WHITE}Enter your choice (1-5): {Colors.RESET}").strip()

            if choice == "1":
                list_recipes()

            elif choice == "2":
                try:
                    num = input(f"\n{Colors.WHITE}Enter recipe number (1-{len(RECIPES)}): {Colors.RESET}").strip()
                    show_recipe(int(num))
                except ValueError:
                    print(f"\n{Colors.RED}Please enter a valid number.{Colors.RESET}")

            elif choice == "3":
                ingredient = input(f"\n{Colors.WHITE}Enter ingredient to search: {Colors.RESET}").strip()
                search_ingredient(ingredient)

            elif choice == "4":
                set_measurement()

            elif choice == "5":
                print(f"\n{Colors.YELLOW}{'═' * 60}{Colors.RESET}")
                print(f"{Colors.GREEN}{Colors.BOLD}  Thank you for using Indian Recipe Cookbook!{Colors.RESET}")
                print(f"{Colors.CYAN}  Happy cooking and enjoy your meal! 🙏 🍛{Colors.RESET}")
                print(f"{Colors.YELLOW}{'═' * 60}{Colors.RESET}\n")
                break

            else:
                print(f"\n{Colors.RED}Invalid choice. Please enter a number between 1 and 5.{Colors.RESET}")

        except KeyboardInterrupt:
            print(f"\n\n{Colors.YELLOW}Exiting... Goodbye! 🙏{Colors.RESET}\n")
            break
        except Exception as e:
            print(f"\n{Colors.RED}An error occurred: {e}{Colors.RESET}")
if __name__ == "__main__":
    main()
