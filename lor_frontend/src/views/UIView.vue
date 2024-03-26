<template>
    <!-- <HeaderVue /> -->
    <div class="container">
        
        <div class="left-div">
            <ChampionListVue />
        </div>
        <div class="right-div">
            <FilterVue v-on:generate="generate" v-on:filterUpdate="filterUpdate" ref="filterVue"/>
        </div>
    </div>
</template>

<script>
import ChampionListVue from './ChampionListVue.vue';
import FilterVue from './FilterVue.vue';
// import HeaderVue from './HeaderVue.vue';

export default {
    name: 'UIView',
    components: {
        ChampionListVue,
        FilterVue,
        // HeaderVue,
    },
    data() {
        return {
            showFilters: false,
            year: 2009,
            filters : {
                
            },
        }
    },
    methods: {
        generate(id) {
            this.id = id;
            this.sendFilters();
        },
        async sendFilters() {
            try{
                const id_response = await fetch('http://localhost:8000/random_champion', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify({
                        id: this.id,
                        banlist: []
                    })
                });
                const id_data = await id_response.json();
                this.$refs.filterVue.updateChampion(id_data);
            } catch (error) {
                console.error(error);
            }
        },
        filterUpdate(filters) {
            this.filters = filters;
        },
        updateYear(event) {
            this.year = event.target.value;
        },
        toggleFilters() {
            this.showFilters = !this.showFilters;
        }
    }
}
</script>

<style scoped>

.container {
    display: flex;
    max-width: 100%;
}

  
.left-div, .right-div {
    height: 100%;
}

.left-div {
    width: 48%;
}

.right-div {
    width: 52%;
    overflow: hidden;
}

.row {
    flex: 1;
    border: 1px solid black;
}

.content {
    display: flex;
    align-items: center;
}

.large-image {
    width: 75px;
    height: 75px;
}

.small-image {
    width: 50px;
    height: 50px;
}

.spacer {
    flex-grow: 1;
}

</style>