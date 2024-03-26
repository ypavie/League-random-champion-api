<template>
  <header class="page-header">
    <div>
      <img class="logo" src="https://static.wikia.nocookie.net/leagueoflegends/images/2/28/Slayer_icon.png" alt="Logo" />
    </div>
    <nav class="nav-links">
      <router-link to="/">Home</router-link>
      <router-link to="/about">About</router-link>
      <router-link to="/contact">Contact</router-link>
    </nav>
  </header>
</template>

<style scoped>
.page-header {
  background-color: #333;
  padding: 10px 20px;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.logo{
  width: 25px;
  height: 25px;
}

.nav-links router-link {
  color: #fff;
  text-decoration: none;
  margin-left: 20px;
}

.nav-links a:hover {
  text-decoration: underline;
}
</style>
