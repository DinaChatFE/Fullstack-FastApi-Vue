<template>
  <p></p>
  <link
    rel="stylesheet"
    href="https://demos.creative-tim.com/notus-js/assets/vendor/@fortawesome/fontawesome-free/css/all.min.css"
  />

  <section class="pt-16 bg-blueGray-50">
    <div id="app">
      <!-- use the modal component, pass in the prop -->
      <modal v-if="showModal" @close="showModal = false">
        <template v-slot:header>
          <h5 class="font-bold uppercase text-lg">Edit profile</h5>
        </template>
        <template v-slot:body>
          <register :close="showModal" @close-modal="showModal = false" />
        </template>
      </modal>
    </div>
    <div class="w-full lg:w-4/12 px-4 mx-auto">
      <div
        class="
          relative
          flex flex-col
          min-w-0
          break-words
          bg-white
          w-full
          mb-6
          shadow-xl
          rounded-lg
          mt-16
        "
      >
        <div class="px-6 relative">
          <button
            @click="alert"
            class="
              absolute
              top-0
              right-0
              p-2
              hover:bg-gray-100
              rounded-full
              duration-100
            "
          >
            <svg
              xmlns="http://www.w3.org/2000/svg"
              class="h-6 w-6"
              fill="none"
              viewBox="0 0 24 24"
              stroke="currentColor"
            >
              <path
                stroke-linecap="round"
                stroke-linejoin="round"
                stroke-width="2"
                d="M17 16l4-4m0 0l-4-4m4 4H7m6 4v1a3 3 0 01-3 3H6a3 3 0 01-3-3V7a3 3 0 013-3h4a3 3 0 013 3v1"
              />
            </svg>
          </button>
          <div class="flex flex-wrap justify-center">
            <div class="w-full px-4 flex justify-center">
              <img
                alt=""
                :src="imageUrl"
                class="
                  shadow-2xl
                  rounded-full
                  align-middle
                  w-36
                  h-36
                  object-cover
                  border-none
                  absolute
                  -m-16
                  -ml-20
                  lg:-ml-16
                "
              />
            </div>

            <div class="w-full px-4 text-center mt-20">
              <div class="flex justify-center py-4 lg:pt-4 pt-8"></div>
            </div>
          </div>
          <h3
            class="
              text-xl
              font-semibold
              leading-normal
              mb-2
              text-blueGray-700
              mb-2
            "
          >
            {{ auth.profile.full_name }}
          </h3>
          <div class="w-2/3 mx-auto">
            <button
              @click="showModalHandler"
              class="
                bg-gray-200
                px-4
                py-2
                rounded-sm
                hover:bg-gray-300
                duration-75
              "
            >
              Edit
            </button>
          </div>

          <div class="flex justify-center align-middle pb-10">
            <div class="text-left mt-12">
              <div
                class="
                  text-sm
                  leading-normal
                  mt-0
                  mb-2
                  text-blueGray-400
                  uppercase
                "
              >
                <i
                  class="fas fa-map-marker-alt mr-2 text-lg text-blueGray-400"
                ></i>
                &nbsp; {{ auth.profile.address }}
              </div>
              <div class="mb-2 text-blueGray-600">
                <i class="fas fa-table text-lg text-blueGray-400"> </i> 
                &nbsp; {{ auth.profile.date_of_birth }}
              </div>
              <div class="mb-2 text-blueGray-600">
                <i class="fas fa-university mr-2 text-lg text-blueGray-400"></i>
                &nbsp;{{ auth.profile.school_work }}
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
    <footer class="relative pt-8 pb-6 mt-8">
      <div class="container mx-auto px-4">
        <div
          class="flex flex-wrap items-center md:justify-between justify-center"
        ></div>
      </div>
    </footer>
  </section>
  <!-- app -->
</template>
<script>
import { useStore } from "vuex";
import { LOG_OUT } from "../store/type";
import { computed } from "vue-demi";
import Modal from "../components/Modal.vue";
import Register from "./Patial/Register.vue";

export default {
  components: { Modal, Register },
  data() {
    const store = useStore();
    return {
      showModal: false,
      auth: computed(() => store.state.auth),
      logOutApi() {
        store.dispatch(LOG_OUT);
        window.location.href = "/";
      },
    };
  },
  methods: {
    showModalHandler() {
      this.showModal = true;
    },
    alert: function () {
      this.$swal
        .fire({
          title: "Are you sure to log out?",
          showCancelButton: true,
          confirmButtonText: "Yes",
        })
        .then((result) => {
          /* Read more about isConfirmed, isDenied below */
          if (result.isConfirmed) {
            this.$swal.fire("Logout success", "", "success");
            this.logOutApi();
          } else if (result.isDenied) {
            this.$swal.fire("Changes are not saved", "", "info");
          }
        });
    },
  },
  watch: {
    showModal: function (val) {
      if (val) {
        document.body.style.overflow = "hidden";
      } else {
        document.body.style.overflow = "auto";
      }
    },
  },
  computed: {
    imageUrl: function () {
       return this.auth.profile.profile ? process.env.VUE_APP_STORAGE + this.auth.profile.profile: "https://cdn.pixabay.com/photo/2015/10/05/22/37/blank-profile-picture-973460_1280.png"
    },
  },

  async created() {
    if (!this.auth.is_auth) {
      // route.push("/");
    }
  },
};
</script>

<style>
.vue-notification {
  margin: 0 5px 5px;
  padding: 10px;
  font-size: 12px;
  color: #ffffff;
  background: #44a4fc !;
  border-left: 5px solid #187fe7;
  border-radius: 30px;
  padding: 10px;
}
.notification-title {
  text-transform: uppercase;
  font-size: 1rem;
  font-weight: bold;
}
.success {
  background: #68cd86;
  border-left: 4px solid #42a85f;
  padding: 10px 12px;
  box-shadow: 5px 15px #42a85f;
}

.warn {
  background: #ffb648;
  padding: 10px 12px;
  border-left: 4px solid #e09016;
  border-left-color: #f48a06;
}

.error {
  background: #e54d42;
  border-left-color: #b82e24;
}
</style>