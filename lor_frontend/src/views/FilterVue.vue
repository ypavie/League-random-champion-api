<template>
    <div class="filters-container">
        <div class="filter-div">
            <div v-if="Object.keys(currentChampion).length > 0" class="images-row">
                <div class="first-row">
                    <div class="image-part">
                        <img class="large-image" :src="currentChampion.icon" :title="formatTitle(currentChampion.name)">
                    </div>
                    <div class="image-part">
                        <div class="name">{{ currentChampion.name }}</div>
                    </div>
                    <div class="image-part">
                        <img class="small-image" :src="currentChampion.summoner_spell_1[1]" :title="formatTitle(currentChampion.summoner_spell_1[0])">
                        <img class="small-image" :src="currentChampion.summoner_spell_2[1]" :title="formatTitle(currentChampion.summoner_spell_2[0])">
                    </div>
                </div>
                <div class="first-row">
                    <div class="image-part">
                        <div style="position: relative;">
                            <img class="small-image" :src="currentChampion.spell_to_max[1]" :title="formatTitle(currentChampion.spell_to_max[0])">
                            <span class="image-overlay">{{ currentChampion.spell_to_max[0] }}</span>
                        </div>
                    </div>
                    <div class="image-part">
                        <img class="small-image" :src="currentChampion.item_1[1]" :title="formatTitle(currentChampion.item_1[0])">
                        <img class="small-image" :src="currentChampion.item_2[1]" :title="formatTitle(currentChampion.item_2[0])">
                        <img class="small-image" :src="currentChampion.item_3[1]" :title="formatTitle(currentChampion.item_3[0])">
                        <img class="small-image" :src="currentChampion.item_4[1]" :title="formatTitle(currentChampion.item_4[0])">
                        <img class="small-image" :src="currentChampion.item_5[1]" :title="formatTitle(currentChampion.item_5[0])">
                        <img class="small-image" :src="currentChampion.item_6[1]" :title="formatTitle(currentChampion.item_6[0])">
                    </div>
                </div>
            </div>
        </div>

        <div class="button-container">
            <button class="button-generate" @click="generate">GENERATE</button>
            <span class="more-filters-text" @click="toggleFilters">{{ showFilters ? 'Less filters' : 'More filters' }}</span>
        </div>
        <div v-show="showFilters">
            <div v-show="showFilters">
                <div class="additional-filters">
                    <div>
                        <div v-for="(tag, key) in tags" :key="key" class="filter">
                            <label>{{ key }}:</label>
                            <template v-if="filterType.radio.includes(key)">
                                <!-- Render radio inputs -->
                                <input type="radio" :id="`${key}_any`" :name="key" value="any" v-model="filters[key]">
                                <label :for="`${key}_any`" class="radio-label">Any</label>
                                <template v-for="tagItem in tag" :key="tagItem">
                                    <input type="radio" :id="`${key}_${tagItem}`" :name="key" :value="tagItem" v-model="filters[key]">
                                    <label :for="`${key}_${tagItem}`" class="radio-label">{{ tagItem }}</label>
                                </template>
                            </template>
                            <template v-else-if="filterType.select.includes(key)">
                                <!-- Render select input -->
                                <select :id="`${key}`" :name="key" class="filter-select" v-model="filters[key]">
                                    <option value="any">Any</option>
                                    <template v-for="tagItem in tag" :key="tagItem">
                                        <option :value="tagItem">{{ tagItem }}</option>
                                    </template>
                                </select>
                            </template>
                        </div>

                        <div class="filter">
                            <label>Release year:</label>
                            <output><label>{{ year }}</label></output>
                            <input type="range" v-model="filters['Release year']" min="2009" :max="new Date().getFullYear()" class="year-slider" @input="updateYear" >
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>
  
<script>
  export default {
    name: "App",
    data() {
      return {
        currentChampion: {},
        showFilters: false,
        year: 2009,
        waitingForResponse: false,
        filters : {
            
        },
        
        filterType: {
            "select": ["Species", "Region",],
            "radio": ["Gender", "Class", "Mana source", "Range",],
        },
        tags: {
            "Class":[
                "Assassin",
                "Fighter",
                "Mage",
                "Marksman",
                "Support",
                "Tank",
            ],
            "Region": [
                "Bandle City",
                "Bilgewater",
                "Camavor",
                "Demacia",
                "Freljord",
                "Icathia",
                "Ionia",
                "Ixtal",
                "Noxus",
                "Piltover",
                "Runeterra",
                "Shadow Isles",
                "Shurima",
                "Targon",
                "Void",
                "Zaun",
            ],
            "Gender": [
                "Female",
                "Male",
                "Other",
            ],
            "Species": [
                "Aspect",
                "Brackern",
                "Cat",
                "Celestial",
                "Chemically Altered",
                "Cyborg",
                "Darkin",
                "Demon",
                "Dog",
                "Dragon",
                "God",
                "God-Warrior",
                "Golem",
                "Human",
                "Iceborn",
                "Magically Altered",
                "Magicborn",
                "Minotaur",
                "Rat",
                "Revenant",
                "Spirit",
                "Spiritualist",
                "Troll",
                "Undead",
                "Unknown",
                "Vastayan",
                "Void-Being",
                "Yordle",
            ],
            "Mana source": [
                "Mana",
                "Manaless",
                "Other",
            ],
            "Range": [
                "Melee",
                "Ranged",
            ],
        }
      };
    },
    methods: {
        toggleFilters() {
            this.showFilters = !this.showFilters;
        },
        generate() {
            // send filters to parent
            if (this.waitingForResponse) {
                return;
            }
            this.$emit('generate', 0);
            this.waitingForResponse = true;

            // reset waitingForResponse after 2 seconds to allow for another request
            setTimeout(() => {
                this.waitingForResponse = false;
            }, 2000);
        },
        filterUpdate(){
            // send filters to parent
            this.$emit('filterUpdate', this.filters);
        },
        updateYear(event) {
            this.year = parseInt(event.target.value);
        },
        updateChampion(champion){
            this.currentChampion = champion;
            this.waitingForResponse = false;
            // add to url the champion id
            this.$router.push({ path: `/${champion.unique_id}` });
        },
        formatTitle(title) {
            title = title.replace(/_/g, ' ');
            title = title.replace(/(?:^|\s|['’])(\w)/g, function(match) {
                return match.toUpperCase();
            });
            return title;
        },
        async fetchChampionData(id) {
            // path('champion/<int:id>', views.get_champion),
            try{
                const id_response = await fetch('http://localhost:8000/champion/' + id, {
                    method: 'GET',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                });
                const id_data = await id_response.json();
                this.currentChampion = id_data;
            } catch (error) {
                console.error(error);
            }

        },
    },
    mounted() {
        // extract id from url
        const currentUrl = window.location.href;
        const url = new URL(currentUrl);
        const pathSegments = url.pathname.split('/');
        const id = pathSegments.pop();

        // if id is not empty and is an integer, fetch champion data
        if (id !== '' && !isNaN(id)) {
            this.fetchChampionData(id);
        }

    },

  };
</script>


<style scoped>



.filters-container {
    flex-direction: column;
    padding: 10px;
    margin-top: 10px;
}

.filter {
    display: flex;
    align-items: center;
    margin-bottom: 10px;
    flex-wrap: wrap;
}

.filter label {
    margin-right: 5px;
}

.filter select, .filter input[type="text"] {
    margin-right: 10px;
}

.filter input[type="text"] {
    padding: 5px;
    border-radius: 5px;
    border: 1px solid #ccc;
}

.filter-select {
    padding: 5px;
    border-radius: 5px;
    border: 1px solid #ccc;
    display: block;
}

.filter .year-slider {
    margin-right: 10px;
    cursor: pointer;
    vertical-align: middle;
}

.filter .selected-year {
    font-size: 14px;
    vertical-align: middle;
}


.additional-filters {
    padding: 10px;
    display: inline-block;
}

.filter {
    margin-bottom: 10px;
}

label {
    display: block;
}

.radio-label {
    display: inline-block;
    padding: 3px 8px;
    border: 1px solid #ccc;
    border-radius: 5px;
    cursor: pointer;
    color: black;
    background-color: white;
    font-size: 14px;
}

.radio-label.disabled {
    background-color: #f1f1f1;
    color: #999;
}

input[type="radio"] {
    display: none;
}

input[type="radio"]:checked + .radio-label {
    background-color: lightgreen;
    color: black;
}

.button-container {
    display: flex;
    justify-content: center;
    align-items: center;
    flex-direction: column;
}

.button-generate {
    margin-bottom: 10px;
    width: 30%;
}

.images-row {
    display: flex;
    justify-content: center;
    align-items: center;
    padding: 10px;
}

.additional-filters {
    padding: 10px;
}

.images-row {
    display: flex;
    flex-direction: column;
}

.first-row {
    display: flex;
    justify-content: center;
    align-items: center;
    margin-bottom: 10px; 
    width: 100%;
}

.image-part {
    width: 100%;
    display: flex;
    justify-content: center;
    align-items: center;
}

.large-image {
    width: 75px;
    height: 75px;
    margin-right: 10px; 
    border: 2px solid black;
}

.small-image {
    width: 50px;
    height: 50px;
    margin-right: 10px; 
    border: 2px solid black;
}

.name {
    margin-right: 10px; 
    text-transform: uppercase;
}

.image-with-overlay {
        position: relative;
    }

    .image-overlay {
        position: absolute;
        bottom: 0;
        left: 0;
        color: white;
        font-size: 22px;
        font-weight: bold;
        padding: 5px;
    }


.radio-label:active {
    transform: scale(1.1);
}

</style>
  