<template>
  <!-- RANDOM CHAMPION -->
  <div class="flex justify-center" v-if="currentChampion.name">
    
    <!-- ICONS-->
    <div class="flex flex-wrap justify-center w-full sm:w-auto">
      
        <!-- CHAMPION ICON -->
      <div class="flex flex-wrap justify-center mb-4">
        <div class="text-center">
          <img :src="currentChampion.icon" :alt=currentChampion.name class="w-16 h-16 md:w-24 md:h-24 mr-4 border-2 border-black rounded-lg">
        </div>
      </div>
      
        <!-- CHAMPION NAME -->
      <div class="flex flex-wrap justify-center items-center mb-4 mx-4">
        <div class="text-center">
          <h2 class="text-2xl font-bold uppercase text-center dark:text-white"> {{ currentChampion.name.replace(/([A-Z])/g, ' $1').trim() }}</h2>
          </div>
        </div>
      
    <!-- SUMMONER SPELLS -->
    <div class="flex flex-wrap justify-center items-center space-x-4 mb-4 mx-4" :class="{ 'disabled-img': !isFilterTypeSelected('summs') }">
        <div class="text-center">
          <img :src="currentChampion.summoner_spell_1[1]" alt="Summoners spell 1" class="w-16 h-16 item-icon border-2 border-black rounded-lg">
        </div>
        <div class="text-center">
          <img :src="currentChampion.summoner_spell_2[1]" alt="Summoners spell 2" class="w-16 h-16 item-icon border-2 border-black rounded-lg">
        </div>
      </div>
      
        <!-- SPELL TO MAX -->
      <div class="flex flex-wrap justify-center items-center space-x-4 mb-4 mx-4 relative">
        <div class="text-center relative">
          <img :src="currentChampion.spell_to_max[1]" alt="Spell to max" class="w-16 h-16 border-2 border-black rounded-lg">
          <span class="absolute bottom-0 left-1 bg-gray-800 bg-opacity-50 text-white text-xl font-bold px-1 py-0.5">{{ convertSpellToMax(currentChampion.spell_to_max[0]) }}</span>
        </div>
      </div>

        <!-- ROLE -->
      <div class="flex flex-wrap justify-center items-center space-x-4 mb-4 mx-4" :class="{ 'disabled-img': !isFilterTypeSelected('roles') }">
        <div class="text-center">
          <img :src="currentChampion.role[1]" alt="Role" class="w-16 h-16 md:w-20 md:h-20 mr-4">
        </div>
      </div>

        <!-- ITEMS -->
      <div class="flex flex-wrap justify-center items-center mb-4 mx-4 mt-4" :class="{ 'disabled-img': !isFilterTypeSelected('items') }">
        <img :src="currentChampion.item_1[1]" alt="Items 1" class="w-16 h-16 border-2 border-black rounded-lg mr-1">
        <img :src="currentChampion.item_2[1]" alt="Items 2" class="w-16 h-16 border-2 border-black rounded-lg mr-1">
        <img :src="currentChampion.item_3[1]" alt="Items 3" class="w-16 h-16 border-2 border-black rounded-lg mr-1">
        <img :src="currentChampion.item_4[1]" alt="Items 4" class="w-16 h-16 border-2 border-black rounded-lg mr-1">
        <img :src="currentChampion.item_5[1]" alt="Items 5" class="w-16 h-16 border-2 border-black rounded-lg mr-1">
        <img :src="currentChampion.item_6[1]" alt="Items 6" class="w-16 h-16 border-2 border-black rounded-lg mr-2">
        <div class="text-center relative">
            <img :src="currentChampion.starter_item[1]" alt="Starter item" class="w-16 h-16 border-2 border-black rounded-lg ml-12">
            <span class="absolute bottom-0 right-0 bg-gray-800 bg-opacity-50 text-white text-base font-bold px-1 py-0.5">Starter</span>
        </div>
      </div>
    </div>

    <!-- RUNES -->
    <div class="flex flex-wrap justify-center w-full sm:w-auto" :class="{ 'disabled-img': !isFilterTypeSelected('runes') }">
      <div class="runes">
        <div class="runes-primary">
          <div :class="'runes-progress ' + currentChampion.rune_main_tree[0].toLowerCase()" :style="getRuneProgress(currentChampion.rune_main_tree[0], true)">
            <div></div>
          </div>
          <ul class="rune-container">
            <li>
              <div>
                <div :title=currentChampion.rune_main_keystone[0] class="main-keystone">
                  <img :src="currentChampion.rune_main_keystone[1]" height="50" :alt=currentChampion.rune_main_keystone[0] class="rune-icon-keystone">
                  <svg viewBox="0 0 50 50" class="rune-circle">
                    <circle cx="25" cy="25" r="24" stroke-width="3" fill="none" :stroke="'url(#gradient-' + currentChampion.rune_main_tree[0].toLowerCase() + ')'"></circle>
                  </svg>
                </div>
              </div>
            </li>
            <li>
              <div>
                <div :title=currentChampion.rune_main_1[0] class="runes-container">
                  <img :src="currentChampion.rune_main_1[1]" height="35" :alt=currentChampion.rune_main_1[0] class="rune-icon">
                  <svg viewBox="0 0 50 50" class="rune-circle">
                    <circle cx="25" cy="25" r="24" stroke-width="3" fill="none" :stroke="'url(#gradient-' + currentChampion.rune_main_tree[0].toLowerCase() + ')'"></circle>
                  </svg>
                </div>
              </div>
            </li>
            <li>
              <div>
                <div :title=currentChampion.rune_main_2[0] class="runes-container">
                  <img :src="currentChampion.rune_main_2[1]" height="35" :alt=currentChampion.rune_main_2[0] class="rune-icon">
                  <svg viewBox="0 0 50 50" class="rune-circle">
                    <circle cx="25" cy="25" r="24" stroke-width="3" fill="none" :stroke="'url(#gradient-' + currentChampion.rune_main_tree[0].toLowerCase() + ')'"></circle>
                  </svg>
                </div>
              </div>
            </li>
            <li>
              <div>
                <div :title=currentChampion.rune_main_3[0] class="runes-container">
                  <img :src="currentChampion.rune_main_3[1]" height="35" :alt=currentChampion.rune_main_3[0] class="rune-icon">
                  <svg viewBox="0 0 50 50" class="rune-circle">
                    <circle cx="25" cy="25" r="24" stroke-width="3" fill="none" :stroke="'url(#gradient-' + currentChampion.rune_main_tree[0].toLowerCase() + ')'"></circle>
                  </svg>
                </div>
              </div>
            </li>
          </ul>
        </div>

        <div class="runes-secondary">
          <div :class="'runes-progress ' + currentChampion.rune_main_tree[0].toLowerCase()" :style="getRuneProgress(currentChampion.rune_secondary_tree[0], false)">
            <div></div>
          </div>
          <ul class="rune-container">
            <li>
              <div>
                <div :title=currentChampion.rune_secondary_1[0] class="runes-container">
                  <img :src=currentChampion.rune_secondary_1[1] height="35" :alt=currentChampion.rune_secondary_1[0] class="rune-icon">
                  <svg viewBox="0 0 50 50" class="rune-circle">
                    <circle cx="25" cy="25" r="24" stroke-width="3" fill="none" :stroke="'url(#gradient-' + currentChampion.rune_secondary_tree[0].toLowerCase() + ')'"></circle>
                  </svg>
                </div>
              </div>
            </li>
            <li>
              <div>
                <div :title=currentChampion.rune_secondary_2[0] class="runes-container">
                  <img :src=currentChampion.rune_secondary_2[1] height="35" :alt=currentChampion.rune_secondary_2[0] class="rune-icon">
                  <svg viewBox="0 0 50 50" class="rune-circle">
                    <circle cx="25" cy="25" r="24" stroke-width="3" fill="none" :stroke="'url(#gradient-' + currentChampion.rune_secondary_tree[0].toLowerCase() + ')'"></circle>
                  </svg>
                </div>
              </div>
            </li>
          </ul>
        </div>

        <div class="runes-stats">
          <ul class="rune-container">
            <li>
              <div :title=currentChampion.rune_shard_1[0] class="runes-container">
                <img :src="currentChampion.rune_shard_1[1]" height="35" :alt=currentChampion.rune_shard_1[0] class="rune-icon">
                <svg viewBox="0 0 50 50" class="rune-circle">
                  <circle cx="25" cy="25" r="24" stroke-width="3" fill="none" stroke="url(#gradient-stats)"></circle>
                </svg>
              </div>
            </li>
            <li>
              <div :title=currentChampion.rune_shard_2[0] class="runes-container">
                <img :src="currentChampion.rune_shard_2[1]" height="35" :alt=currentChampion.rune_shard_2[0] class="rune-icon">
                <svg viewBox="0 0 50 50" class="rune-circle">
                  <circle cx="25" cy="25" r="24" stroke-width="3" fill="none" stroke="url(#gradient-stats)"></circle>
                </svg>
              </div>
            </li>
            <li>
              <div :title=currentChampion.rune_shard_3[0] class="runes-container">
                <img :src="currentChampion.rune_shard_3[1]" height="35" :alt=currentChampion.rune_shard_3[0] class="rune-icon">
                <svg viewBox="0 0 50 50" class="rune-circle">
                  <circle cx="25" cy="25" r="24" stroke-width="3" fill="none" stroke="url(#gradient-stats)"></circle>
                </svg>
              </div>
            </li>
          </ul>
        </div>

        <svg width="0" height="0">
          <linearGradient id="gradient-precision" x1="0" y1="0" x2="1" y2="1">
            <stop stop-color="#c8aa6e" offset="0%"></stop>
            <stop stop-color="#aea789" offset="100%"></stop>
          </linearGradient>
          <linearGradient id="gradient-domination" x1="0" y1="0" x2="1" y2="1">
            <stop stop-color="#ca3e3f" offset="0%"></stop>
            <stop stop-color="#dc4747" offset="100%"></stop>
          </linearGradient>
          <linearGradient id="gradient-sorcery" x1="0" y1="0" x2="1" y2="1">
            <stop stop-color="#9faafc" offset="0%"></stop>
            <stop stop-color="#6c75f5" offset="100%"></stop>
          </linearGradient>
          <linearGradient id="gradient-resolve" x1="0" y1="0" x2="1" y2="1">
            <stop stop-color="#a1d586" offset="0%"></stop>
            <stop stop-color="#a4d08d" offset="100%"></stop>
          </linearGradient>
          <linearGradient id="gradient-inspiration" x1="0" y1="0" x2="1" y2="1">
            <stop stop-color="#49aab9" offset="0%"></stop>
            <stop stop-color="#48b4be" offset="100%"></stop>
          </linearGradient>
          <linearGradient id="gradient-stats" x1="0" y1="0" x2="1" y2="1">
            <stop stop-color="#c8aa6e" offset="0%"></stop>
            <stop stop-color="#aea789" offset="100%"></stop>
          </linearGradient>
        </svg>

      </div>

    </div>
    
  </div>
  <!-- FILTERS -->
  <div class="mt-8">
    <Filters @update-filter="updateFilter" @input-change="inputChange" @select-all="selectAll" @unselect-all="unselectAll" @generate="generate" ref="Filters" />
  </div>
</template>
<script>
import Filters from '../filters/Filters.vue'

export default {
    name: 'GenerateRandomChampion',
    emits: ['update-filter', 'input-change', 'select-all', 'unselect-all', 'generate'],

    components: {
        Filters,
    },
    data() {
        return {
            currentChampion: {},
            selectedFiltersTypes: {
                champion: true,
                roles: true,
                runes: true,
                items: true,
            }
        }
    },
    methods: {
        updateCurrentChampion(champion) {
            this.currentChampion = champion;
            this.selectedFiltersTypes = this.$refs.Filters.getSelectedFiltersTypes();
        },
        updateFilter(filters) {
            this.$emit('update-filter', filters);
        },
        inputChange(searchTerm) {
            this.$emit('input-change', searchTerm);
        },
        selectAll() {
            this.$emit('select-all');
        },
        unselectAll() {
            this.$emit('unselect-all');
        },
        generate() {
            this.$emit('generate');
        },
        getRuneProgress(rune, type) {
            if (type) {
                return {
                    height: '150px',
                    background: 'url(#gradient-' + rune.toLowerCase() + ')',
                }
            } else {
                return {
                    height: '50px',
                    background: 'url(#gradient-' + rune.toLowerCase() + ')',
                }
            }
        },
        parseName(name) {
            return name.replace(/_/g, ' ').replace(/(?:^|\s)\S/g, function(a) { return a.toUpperCase(); });
        },
        convertSpellToMax(spell) {
            switch (spell) {
                case 0:
            return 'Q';
                case 1:
            return 'W';
                case 2:
            return 'E';
                default:
            return 'Q';
            }
        },
        isFilterTypeSelected(type) {
            return this.selectedFiltersTypes[type];
        },
        getSelectedLanes() {
            return this.$refs.Filters.getSelectedLanes();
        }
    }
}
</script>

<style scoped>

.text-center:hover p {
  display: block;
}

.runes {
  display: flex;
  margin-top: 20px;
}

.runes-primary {
  display: flex;
  flex-direction: column;
  position: relative;
}

.runes-progress {
  position: absolute;
  left: 23px;
  top: 50px;
  box-shadow: inset 0 0 3px rgba(255, 255, 255, .4);
}

.runes-progress div {
  width: 4px;
}

.runes-secondary {
  min-width: 50px;
  display: flex;
  margin-top: 50px;
  flex-direction: column;
  position: relative;
}

.runes-stats {
  min-width: 50px; 
  display: flex; 
  margin-top: 50px; 
  flex-direction: column; 
  position: relative;
}

.main-keystone{
  width: 50px; 
  height: 50px; 
  margin: 0px auto;
}

.rune-circle{
  position: relative;
}

.rune-icon{
  position: absolute;
  width: 35px;
  height: 35px;
}

.rune-icon-keystone{
  position: absolute;
  width: 50px;
  height: 50px;
}

.rune-container{
  list-style-type: none; 
  padding: 0px;
}
.runes-container{
  width: 35px; 
  height: 35px; 
  margin: 15px auto 0px;
}

.runes-progress.precision {
  background-color: #e7b95d4d;
}

.runes-progress.resolve {
  background-color: #7eb95e;
}

.runes-progress.domination {
  background-color: #e236364d;
}

.runes-progress.inspiration {
  background-color: #56cbdd4d;
}

.runes-progress.sorcery {
  background-color: #7986eb4d;
}

.runes-progress.precision div {
  height: 50px;
  background-color: #e7b95d;
}

.runes-progress.resolve div {
  height: 150px;
  background-color: url(#gradient-resolve);
}

.disabled-img {
  filter: grayscale(100%) brightness(5%);
}

</style>
