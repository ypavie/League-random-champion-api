<template>
  <div class="grid items-center justify-center">
    <div class="flex flex-wrap items-center">
      <!-- LANES -->
      <div class="flex items-center space-x-4 justify-center">
        <img
          v-for="(image, index) in images"
          :key="index"
          :src="image.src"
          :class="[
            'custom-icon',
            'cursor-pointer',
            'h-12 w-12 rounded-full',
            { 'filter grayscale': selected.indexOf(index) === -1, 'transform scale-110': selected.indexOf(index) !== -1 }
          ]"
          @click="toggleSelected(index)"
          alt="Role Image"
        >
      </div>

      <!-- CHAMPION NAME -->
      <div class="flex items-center space-x-4 mr-8 ml-8">
        <input type="text" class="border border-gray-300 dark:border-gray-700 rounded-md pl-6 pr-4 py-2 w-full sm:w-48 focus:outline-none focus:border-blue-500 dark:bg-gray-800 dark:text-white" placeholder="Champion name..." @input="emitInput">
      </div>
      <button @click="selectAll" class="custom-button ml-2 bg-gray-200 dark:bg-gray-700 hover:bg-gray-300 dark:hover:bg-gray-600 text-gray-700 dark:text-white font-bold py-2 px-4 rounded">
        Select All
      </button>
      <button @click="unselectAll" class="custom-button ml-2 bg-gray-200 dark:bg-gray-700 hover:bg-gray-300 dark:hover:bg-gray-600 text-gray-700 dark:text-white font-bold py-2 px-4 rounded">
        Unselect All
      </button>
    </div>
    <div class="flex items-center justify-center">
      <button @click="generate" class="mt-4 bg-blue-500 dark:bg-blue-700 hover:bg-blue-600 dark:hover:bg-blue-800 text-white font-bold py-2 px-2 rounded w-32">
        GENERATE
      </button>
    </div>
  </div>
  <AdvancedFilters ref="advancedFilters" @update-filter="updateFilter" />
</template>

<script>
import AdvancedFilters from '../filters/AdvancedFilters.vue'

export default {
  name: 'GenerateRandomChampion',
  emits: ['update-filter', 'input-change', 'select-all', 'unselect-all', 'generate'],
  components: {
    AdvancedFilters
  },
  data() {
    return {
      selected: [0, 1, 2, 3, 4],
      images: [
        { src: 'https://raw.githubusercontent.com/InFinity54/LoL_DDragon/master/extras/lanes/top.png' },
        { src: 'https://raw.githubusercontent.com/InFinity54/LoL_DDragon/master/extras/lanes/jungle.png' },
        { src: 'https://raw.githubusercontent.com/InFinity54/LoL_DDragon/master/extras/lanes/middle.png' },
        { src: 'https://raw.githubusercontent.com/InFinity54/LoL_DDragon/master/extras/lanes/bottom.png' },
        { src: 'https://raw.githubusercontent.com/InFinity54/LoL_DDragon/master/extras/lanes/support.png' }
      ],
    }
  },
  methods: {
    emitInput(event) {
      this.$emit('input-change', event.target.value);
    },
    selectAll() {
      this.$emit('select-all');
    },
    unselectAll() {
      this.$emit('unselect-all');
    },
    generate(filters) {
      this.$emit('generate', filters);
    },
    updateFilter(filter) {
      this.$emit('update-filter', filter);
    },
    toggleSelected(index) {
      const selectedIndex = this.selected.indexOf(index);
      if (selectedIndex === -1) {
        this.selected.push(index);
      } else {
        this.selected.splice(selectedIndex, 1);
    }
  }
  }
}
</script>

<style scoped>
.custom-icon {
  cursor: pointer;
  transition: transform 0.3s ease;
  transform-origin: center;
}
.custom-icon:hover {
  transform: scale(1.1);
}

.custom-icon:active {
  transform: scale(0.9);
}

.custom-button {
  background-color: #ccc;
  color: #333;
  font-weight: bold;
  padding: 0.5rem 1rem;
  /* border-radius: 0.25rem; */
  cursor: pointer;
  transition: background-color 0.3s, transform 0.1s;
}

.custom-button:hover {
  background-color: #ddd;
  transform: scale(1.05);
}

.custom-button:active {
  transform: scale(0.95);
}


</style>
