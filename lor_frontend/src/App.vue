<template>
    <AppHeader />
    <div class="grid grid-cols-1 md:grid-cols-10 gap-4 mx-auto md:h-[93.5vh] bg-white py-10 px-4 sm:px-6 lg:px-8 dark:bg-gray-800">
        <div class="col-span-1 md:col-span-6 p-4 overflow-y-auto border border-gray-200 dark:border-gray-700 rounded-lg">
            <GenerateRandomChampion ref="generateRandomChampion" 
                @update-filter="updateFilters"
                @input-change="updateSearchTerm"
                @select-all="selectAll"
                @unselect-all="unselectAll"
                @generate="generate"
            /> 
        </div>
        <div class="col-span-1 md:col-span-4 overflow-y-auto">
            <ChampionList 
                :champions="champions" 
                @bannedChampions="updateBannedChampions"
                ref="championList"
            />
        </div>
    </div>
    <AppFooter />
</template>
  

<script>

import ChampionList from './view/main/ChampionList.vue'
import GenerateRandomChampion from './view/main/GenerateRandomChampion.vue'
import AppHeader from './view/layout/AppHeader.vue'
import AppFooter from './view/layout/AppFooter.vue'

export default {
  components: {
    AppHeader,
    AppFooter,
    ChampionList,
    GenerateRandomChampion,
  },
  data() {
        return {
            showFilters: false,
            year: 2009,
            filters: {},
            champions: [],
            filteredChampions: {},
            bannedChampions: [],
            currentSearchTerm: '',
        }
    },
    methods: { 
        sendChampionListFiltered(filters) {
            const filteredChampions = this.updateFilters(filters);
            if (this.currentSearchTerm !== '') {
                for (const championKey in this.champions) {
                    if (championKey.toLowerCase().includes(this.currentSearchTerm.toLowerCase())) {
                        filteredChampions[championKey] = this.champions[championKey];
                    }
                }
            }
            this.$refs.championList.updateFilteredlist(filteredChampions);
        },
        async loadChampions() {
            try {
                const response = await fetch('http://localhost:8000/data/champions');
                const data = await response.json();
                this.champions = data;
            } catch (error) {
                console.error(error);
            }
        },
        async loadCurrentChampionFromURL() {
            const id = window.location.pathname.split('/').pop();
            if (id) {
                try {
                    const id_response = await fetch('http://localhost:8000/champion/' + id);
                    const id_data = await id_response.json();
                    this.$refs.generateRandomChampion.updateCurrentChampion(id_data);
                } catch (error) { }
            }
        },
        async generate() {
            const allowedChampionList = this.getAllowedChampionlist();
            try {
                const id_response = await fetch('http://localhost:8000/random_champion', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify({
                        allowedChampionList: allowedChampionList
                    })
                });
                const data = await id_response.json();
                const id = data.unique_id;
                this.$router.push('/' + id);
                this.$refs.generateRandomChampion.updateCurrentChampion(data);
            } catch (error) {
                console.error(error);
            }
        },
        selectAll() {
            this.$refs.championList.updateBanlist({});
        },
        unselectAll() {
            this.$refs.championList.updateBanlist(this.champions);
        },
        updateSearchTerm(searchTerm) {
            this.currentSearchTerm = searchTerm;
            const filteredChampions = this.getFilterList();
            this.$refs.championList.updateFilteredlist(filteredChampions);
        },
        updateFilters(filters) {
            this.filters = filters;
            const filteredChampions = this.getFilterList();
            this.$refs.championList.updateFilteredlist(filteredChampions);
        },
        updateBannedChampions(bannedChampions) {
            this.bannedChampions = bannedChampions;
        },
        getFilterList() {
            const filteredChampions = {};
            for (const championKey in this.champions) {
                if (championKey.toLowerCase().includes(this.currentSearchTerm.toLowerCase())) {
                    filteredChampions[championKey] = this.champions[championKey];
                }
            }

            for (const championKey in filteredChampions) {
                let championMatchesFilters = true;
                for (const filterKey in this.filters) {
                    const filterValue = this.filters[filterKey];
                    const championValue = this.champions[championKey][filterKey];
                    if (filterValue !== '') {
                        if (Array.isArray(championValue)) {
                            if (!championValue.includes(filterValue)) {
                                championMatchesFilters = false;
                                break;
                            }
                        } else {
                            if (championValue != filterValue) {
                                championMatchesFilters = false;
                                break;
                            }
                        }
                    }
                }
                if (!championMatchesFilters) {
                    delete filteredChampions[championKey];
                }
            }
            return filteredChampions;
        },
        getAllowedChampionlist() {
            const filteredChampions = this.getFilterList();
            const banlist = Object.keys(filteredChampions).filter(champion => this.bannedChampions.includes(champion));
            const allowedChampionlist = Object.keys(filteredChampions).filter(champion => !banlist.includes(champion));
            return allowedChampionlist;
        }

    },
    mounted() {
        this.loadChampions();
        this.loadCurrentChampionFromURL();
    }
  }

</script>

<style>
body {
    overflow: hidden;
}

@media only screen and (max-width: 768px) {
    body {
        overflow: auto;
    }
}

</style>
