<template>
    <!--    Nav bar-->
    <nav class="navbar navbar-expand-md navbar-dark bg-dark sticky-top">
      <a class="navbar-brand" href="#">
        <img alt="Aux delices de sharon" height="34" src="static/media/logorestaurant.jpg" width="38">
      </a>
      <button class="navbar-toggler" data-target="#navbarCollapse" data-toggle="collapse" type="button">
        <span class="navbar-toggler-icon"/>
      </button>

      <div class="collapse navbar-collapse" id="navbarCollapse">

        <!-- Dynamic part of the navbar, it depends on the navigation prop -->
        <div class="navbar-nav ">
          <div v-for="(navElement, index) in navigation" :key="'navbar-root-' + index">
            <!-- Two types of elements can be rendered, composite and and single item-->
            <a v-if="!navElement.children"
               class="nav-item nav-link"
               :href="navElement.id">
              {{navElement.name}}
            </a>

            <!-- Composite navigation element -->
            <div v-else class="nav-item dropdown">
              <a
                class="nav-link dropdown-toggle"
                data-toggle="dropdown"
                :href="navElement.id"
              >
                {{ navElement.name }}
              </a>
              <div class="dropdown-menu">
                <a
                  v-for="(child, childIndex) in navElement.children"
                  class="dropdown-item"
                  :href="child.id"
                  :key="'navbar-root-' + index + '-' + childIndex"
                >
                  {{ child.name }}
                </a>
              </div>
            </div>
          </div>
        </div>

        <!-- Login and registration links are always here -->
        <div class="navbar-nav ml-auto">
          <a
            class="nav-item nav-link"
            href="login.html"
          >Login</a>
          <a
            class="nav-item nav-link"
            href="register.html"
          >Sign up</a>
        </div>
      </div>
    </nav>
</template>

<script>
export default {
  name: 'Navbar',
  props: ['navigation']
}
</script>

<style scoped>

</style>
