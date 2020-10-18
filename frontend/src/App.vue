<template>
  <div id="app">
    <Navbar :navigation="navigation" :menus="menus"/><br>

    <!--welcome page details-->
    <Welcome title="The History of the restaurant" image="static/media/referenceboss.jpg" id="welcome">
      <p>
      Welcome to Aux delices de Sharon. The restaurant was set up by Marthe Coubard who is a student in
      ICT at ARU .
      Marthe chose the ICT background at ARU because she want to be a web developer. Thanks to this
      background, she decided to set up her own web application.
      Her web application is about restaurant. Marthe loves cooking, and sharing her secrets of cooking.
      The love of cooking started since marthe was teenager.
      Marthe's mother loves cooking Africa food, she shares her secret to marthe who decided to cook
      European Food instead of Africa food because when marthe arrived at France, she fall in love with
      the French Food.
      Today, marthe decided to open a restaurant called Aux delices de Sharon, the restaurant made diverse
      varities of Food from different countries in Europe such as French, Spanish, Italia etc.
      To improve her image, the restaurant open a cooking class in which people can subscribe to learn how
      to cook some courses and also teach people about the name of courses, the purpose is to share
      marthe's cooking secret with her customers.
      Through her Gallery page or restaurant service (lunch, dinner, menu),you can learn the name of
      courses.
      The restaurant offer a booking table, a visualization lunch, dinner or menu card into restaurant
      field and delivery page . For any book for event or cooking class
      please check in event field and cooking class to find any information that you need.
      </p>
    </Welcome>

    <br>

    <!--Lunch daily specials -->
    <SpecialPresentation title="Lunch Dishes" :specials="menus.lunchSpecials" id="lunch_presentation">
      <p>
        For every day in week, we offer an unique dish for Lunch. So if you book for table for monday for instance,
        the restaurant will offer you the Monday dish day or the menu card on below
        as your meal. Please find the name of the dish on footer of the dish's image and his price in pounds (£)
      </p>
    </SpecialPresentation>

    <br>

    <!--Dinner daily specials -->
    <SpecialPresentation title="Dinner Dishes" :specials="menus.dinnerSpecials" id="dinner_presentation">
      <p>
        For every day in week, we offer an unique dish for Lunch. So if you book for table for monday for instance,
        the restaurant will offer you the Monday dish day or the menu card on below
        as your meal. Please find the name of the dish on footer of the dish's image and his price in pounds (£)
      </p>
    </SpecialPresentation>

    <br>

    <!-- Dishes all the time on the menu card -->

    <MenuPresentation title="The Menu Card Dishes" :restaurantMenu="menus.restaurantMenu" id="menu">
       <p>
        Please have a look on our Menu card. Notice that our Menu card is available every day,
        if you don't want any of our lunch or Dinner course, you can choose one of menu course plus any starter,
        dessert and supplement course.
      </p>
    </MenuPresentation>

    <br>

    <!-- booking information-->
    <TableBooking title="Booking for a table" id="table_booking">
      <p>
        Please, fill out this form if you want to book for a table or any other form of booking such as romantic
        lunch or dinner.
        Notice that the romantic lunch or dinner is our VIP service, so please indicate if you booking is VIP or a
        simple table.
        For any other booking for events please click on our events pre-booking to find any information about it.
        The time to booking must be between 12 to 23pm. And the date must be the current day, not the day before. Thank you!
      </p>
    </TableBooking>

    <br>

    <!--delivery for meal form-->
    <DeliveryOrder title="Delivery form for Meals" id="delivery_order" :menus="menus">
      <p>
        Please, fill out this form. To indicate your way of delivery (at restaurant or your place), you must call us.
        For any request please send us an email or call us, we will be delight to answer you.
        Notice that all payment will deal at the delivery.
        Notice also that, the time to book of delivery must between 12 to 16pm or 19 to 23:59 pm.
        The date must be the current day. Thank you!
      </p>
    </DeliveryOrder>

    <br>

    <!--events information-->
    <div class="container" id="events_details">
      <h3 id="events_information">Events details</h3>
      <p>
        Our restaurant offers divers services in events such as Company event or business event, proposal, wedding
        and party such as birthday, celebration, anniversary etc. On below you will find more description about
        each event and the form of pre-booking. For more information, please don't hesitate to contact us.
      </p>
      <br>
      <div class="card-body">
        <EventDescription title="Wedding" image="static/media/wedding-event.jpg">
          Here there is one of the wedding we have organized in January. Notice that the courses we offer
          for the wedding is different for those we pour in the restaurant every day. We cook the
          customer's course
          or offer the customer to choose one of the course in some of our restaurant booking. We can also
          cook the most popular courses in the world
          if the customer claim a request for that. We have a large staff team to you have a great wedding
          event.
          We also work in partnership with some decoration company if you need some idea in wedding
          decoration.
          The restaurant have a big garden available if you want to organize you wedding at the
          restaurant. However, we will be delight
          to make our cooking wedding in your choice place.
        </EventDescription>

        <EventDescription title="Party" image="static/media//party-event.jpg">
          Here there is one of the wedding we have organized in January. Notice that
          the courses we offer
          for the wedding is different for those we pour in the restaurant every day. We cook the
          customer's course
          or offer the customer to choose one of the course in some of our restaurant booking. We can also
          cook the most popular courses in the world
          if the customer claim a request for that. We have a large staff team to you have a great wedding
          event.
          We also work in partnership with some decoration company if you need some idea in wedding
          decoration.
          The restaurant have a big garden available if you want to organize you wedding at the
          restaurant. However, we will be delight
          to make our cooking wedding in your choice place.
        </EventDescription>

        <EventDescription title="Proposal" image="static/media//proposal-event.jpg">
          Here there is one of the wedding we have organized in January. Notice that the courses we offer
          for the wedding is different for those we pour in the restaurant every day. We cook the
          customer's course
          or offer the customer to choose one of the course in some of our restaurant booking. We can also
          cook the most popular courses in the world
          if the customer claim a request for that. We have a large staff team to you have a great wedding
          event.
          We also work in partnership with some decoration company if you need some idea in wedding
          decoration.
          The restaurant have a big garden available if you want to organize you wedding at the
          restaurant. However, we will be delight
          to make our cooking wedding in your choice place.
        </EventDescription>

        <EventDescription title="Business Events" image="static/media//company-party.jpg">
          Here there is one of the wedding we have organized in January. Notice that the courses we offer
          for the wedding is different for those we pour in the restaurant every day. We cook the
          customer's course
          or offer the customer to choose one of the course in some of our restaurant booking. We can also
          cook the most popular courses in the world
          if the customer claim a request for that. We have a large staff team to you have a great wedding
          event.
          We also work in partnership with some decoration company if you need some idea in wedding
          decoration.
          The restaurant have a big garden available if you want to organize you wedding at the
          restaurant. However, we will be delight
          to make our cooking wedding in your choice place.
        </EventDescription>
      </div>

      <br>
      <p> Notice that, to book for an event, the time must be between 14 to 18pm and the date must be 14 day before.</p>
      <EventPreBooking title="Pre-booking" id="event_enrollment"></EventPreBooking>
    </div>

    <br>

    <!--cooking class information-->
    <div class="container" id="cooking_class">
      <h3 id="cooking_class_information">Cooking Class</h3>
      <p>
        In order to be close to our customer, the restaurant decided to offer a cooking class for those who want
        to learn how to make our course. we also offer onlive lesson for those who don't have time to come at
        restaurant to learn.
        To make some of our courses, we were inspired by some cooking book from France, Spain, Italic etc.
        Apart from our cooking creation, we are also trying to imitate the way the best chief in the world make
        their courses.
      </p>

      <div class="card-body ">
        <div class="row">
          <div class="col-lg-6">
            <img src="static/media//kitchen-class.jpg">
          </div>
          <div class="col-lg-6">
<!--            <iframe src="static/media/sample of cooking_lesson.mp4"></iframe>-->
          </div>
        </div>
        <br>

        <h5>Cooking Books</h5>

        <p> Here there is our library book inspiration. Those which we used to made most of our course</p>
        <br>
        <div class="row">
          <div class="col-lg-6" v-for="(book, index) in books" :key="index">
            <p>{{book.description}}</p>
            <img :src="book.img">
          </div>
        </div>
      </div>
      <br>
      <p> Notice that, to booking for a lesson, you must apply three day before</p>
      <CookingClassBooking id="cooking_class_enrolment"/>

    </div>

    <br>

    <hr>
    <!--gallery information-->
    <Gallery/>
    <br>
    <hr>

    <!-- Footer -->
    <footer class="page-footer font-small bg-dark font-weight-normal text-light pt-4">
      <!-- Footer Links -->
      <div class="container">
        <!-- Grid row -->
        <div class="row justify-content-between">
          <!-- Grid column -->
          <div class="col-md-4">
            <!-- Content -->
            <h6 class="font-weight-bold text-uppercase mt-3 mb-4">
              SHARON COOKING RESTAURANT
            </h6>
            <p>
              Welcome AT Sharon Cooking Restaurant. The restaurant offer a large variety of European food.
              Please find above the link of register yourself and earn 5% of reduction.
            </p>
          </div>
          <!-- Grid column -->
          <div class="col-md-4">
            <!-- Links -->
            <h6 class="text-uppercase font-weight-bold" id="contact">
              Contact
            </h6>
            <address>
              12 Kent Way, Cambridge, CB4 2QY, UK
              marthe.ekoule@gmail.com
              + 07 40 37 53 994
            </address>
          </div>
        </div>
      </div>

      <!-- Call to action -->
      <div class="">
      <ul class="list-unstyled list-inline text-center py-2">
        <li class="list-inline-item">
          <h5 class="mb-1">
            Register for free
          </h5>
        </li>
        <li class="list-inline-item">

            <a class="btn btn-danger btn-rounded"
            data-toggle="modal" data-target="#registerModal"
             href="#registerModal"
            id="register">
            Sign up!</a>

        </li>
      </ul>
    </div>
    </footer>

  </div>
</template>

<script>
import RestaurantApi from '@/RestaurantApi'

import EventDescription from '@/components/site/EventDescription'
import Navbar from '@/components/site/Navbar'
import Welcome from '@/components/site/Welcome'
import SpecialPresentation from '@/components/site/SpecialPresentation'
import MenuPresentation from '@/components/site/MenuPresentation'
import TableBooking from '@/components/user/TableBooking'
import DeliveryOrder from '@/components/user/DeliveryOrder'
import EventPreBooking from '@/components/user/EventPreBooking'
import CookingClassBooking from '@/components/user/CookingClassBooking'
import Gallery from '@/components/site/Gallery'
import EventBus from '@/EventBus'
import $ from 'jquery'

export default {
  name: 'App',
  data: function () {
    return {
      // Configuration of the navbar, it contains the name of the link and the id of the link.
      navigation: [
        { name: 'Home', id: '#welcome' },
        {
          name: 'Restaurant',
          id: '',
          children: [
            { name: 'Lunch', id: '#lunch_presentation' },
            { name: 'Dinner', id: '#dinner_presentation' },
            { name: 'Menu', id: '#menu' },
            { name: 'Booking', id: '#table_booking' },
            { name: 'Delivery', id: '#delivery_order' }
          ]
        },
        {
          name: 'Events',
          id: '',
          children: [
            { name: 'Services', id: '#events_information' },
            { name: 'Pre-booking', id: '#event_enrollment' }
          ]
        },
        {
          name: 'Cooking classes',
          id: '',
          children: [
            { name: 'Information', id: '#cooking_class_information' },
            { name: 'Enrolment', id: '#cooking_class_enrolment' }
          ]
        },
        { name: 'Gallery', id: '#Gallery_details' },
        { name: 'Contact', id: '#contact' }
      ],
      menus: {
        dishes: [],
        lunchSpecials: [],
        dinnerSpecials: [],
        restaurantMenu: {}
      },
      books: [
        {
          description: 'Simplissime book is well-know in France for making a quick foods.',
          img: 'static/media//cooking_book1.jpg'
        },
        {
          description: 'The Tapas foods is from spain. The spain food is well-know as a spicy food.',
          img: 'static/media//cooking_book2.jpg'
        },
        {
          description: 'The sous vide book is from France. It is another away to make food by using a spray.',
          img: 'static/media//cooking_book3.jpg'
        },
        {
          description: 'This book is showed all kind of vacuum food people can make in the simple way and faster.',
          img: 'static/media//cooking_book4.jpg'
        }
      ],
      api: RestaurantApi
    }
  },
  methods: {
    // The first thing the client does is get all the dishes served by the restaurant.
    fetchDishes () {
      const app = this
      RestaurantApi.getDishes()
        .then(function (response) {
          // When received, we filter the list of dishes into menus:
          //   - lunchSpecials
          //   - dinnerSpecials
          //   - restaurantMenu (always served)
          // The restaurant menu is divided into starters, mains, sides and dessert
          const dishes = response.data

          app.menus.dishes = dishes

          // All dishes available, filter them and add them to their binding
          app.menus.lunchSpecials = dishes.filter(dish => dish.type === 'special' && dish.serving_time === 'lunch')
          app.menus.dinnerSpecials = dishes.filter(dish => dish.type === 'special' && dish.serving_time === 'dinner')
          app.menus.restaurantMenu = {
            starters: dishes.filter(dish => dish.type === 'starter'),
            mains: dishes.filter(dish => dish.type === 'main'),
            sides: dishes.filter(dish => dish.type === 'side'),
            dessert: dishes.filter(dish => dish.type === 'dessert')
          }
          EventBus.emit(EventBus.MENUS_UPDATED, app.menus)
        })
        .catch(function (error) {
          console.log(error)
        })
    }
  },
  mounted: function () {
    // Executed when the application is mounted into the dom.
    this.fetchDishes()
    const app = this
    EventBus.on(EventBus.DISHES_UPDATES, function () {
      app.fetchDishes()
    })
  },
  computed: {

  },
  /* List of HTML components used to render the HTML */
  components: {
    Gallery,
    CookingClassBooking,
    EventPreBooking,
    DeliveryOrder,
    TableBooking,
    MenuPresentation,
    Welcome,
    SpecialPresentation,
    EventDescription,
    Navbar
  },
  created () {
    // Fix scrolling when one modal overlays another and is closed
    $(document).on('hidden.bs.modal', '.modal', function () {
      $('.modal:visible').length && $(document.body).addClass('modal-open')
    })

    // Adjust the zIndex when one modal overlays another
    $(document).on('show.bs.modal', '.modal', function () {
      const zIndex = 1040 + (10 * $('.modal:visible').length)
      $(this).css('z-index', zIndex)
      setTimeout(function () {
        $('.modal-backdrop').not('.modal-stack').css('z-index', zIndex - 1).addClass('modal-stack')
      }, 0)
    })
  }
}
</script>

<style scoped>

</style>
