<template>
  <div
    class="
      bg-white
      w-full
      px-2
      flex
      items-center
      justify-center
    "
  >
    <div class="w-full relative">
      <form @submit="updateUser" class="mt-6" action="#" method="POST">
        <div class="grid md:grid-cols-2 gap-x-8 gap-y-2 py-4">
          <div>
            <label class="block text-gray-700 text-left">First name</label>
            <input
              v-model="body.first_name"
              @blur="v$.body.first_name.$touch"
              type="text"
              placeholder="Enter First name"
              class="
                w-full
                px-4
                py-2
                rounded-lg
                bg-gray-200
                mt-2
                border
                focus:border-blue-500 focus:bg-white focus:outline-none
              "
            />
            <span
              v-if="v$.body.first_name.$error"
              class="
                flex
                items-center
                font-medium
                tracking-wide
                text-red-500 text-xs
                mt-1
                ml-1
              "
            >
              {{ v$.body.first_name.required.$message }},
            </span>
          </div>
          <div>
            <label class="block text-gray-700 text-left">Last name</label>
            <input
              @blur="v$.body.last_name.$touch"
              v-model="body.last_name"
              type="text"
              placeholder="Enter Last name"
              class="
                w-full
                px-4
                py-2
                rounded-lg
                bg-gray-200
                mt-2
                border
                focus:border-blue-500 focus:bg-white focus:outline-none
              "
            />
            <span
              v-if="v$.body.last_name.$error"
              class="
                flex
                items-center
                font-medium
                tracking-wide
                text-red-500 text-xs
                mt-1
                ml-1
              "
            >
              {{ v$.body.last_name.required.$message }},
            </span>
          </div>

          <div>
            <label class="block text-gray-700 text-left">Date of birth</label>
            <input
              @blur="v$.body.date_of_birth.$touch"
              type="date"
              v-model="body.date_of_birth"
              placeholder="Enter Confirm password"
              minlength="6"
              class="
                w-full
                px-4
                py-2
                rounded-lg
                bg-gray-200
                mt-2
                border
                focus:border-blue-500 focus:bg-white focus:outline-none
              "
            />
            <span
              v-if="v$.body.date_of_birth.$error"
              class="
                flex
                items-center
                font-medium
                tracking-wide
                text-red-500 text-xs
                mt-1
                ml-1
              "
            >
              {{ v$.body.date_of_birth.required.$message }},
            </span>
          </div>
          <div>
            <label class="block text-gray-700 text-left">Bio</label>
            <textarea
              v-model="body.bio"
              placeholder="Enter Bio"
              minlength="6"
              class="
                w-full
                px-4
                py-2
                rounded-lg
                bg-gray-200
                mt-2
                border
                focus:border-blue-500 focus:bg-white focus:outline-none
              "
            ></textarea>
          </div>
          <div>
            <label class="block text-gray-700 text-left">Address</label>
            <textarea
              type="textarea"
              v-model="body.address"
              placeholder="Enter Address"
              minlength="6"
              class="
                w-full
                px-4
                py-2
                rounded-lg
                bg-gray-200
                mt-2
                border
                focus:border-blue-500 focus:bg-white focus:outline-none
              "
            ></textarea>
          </div>
          <div>
            <label class="block text-gray-700 text-left">School or Work</label>
            <textarea
              
              v-model="body.school_work"
              placeholder="Enter School or Work"
              minlength="6"
              class="
                w-full
                px-4
                py-2
                rounded-lg
                bg-gray-200
                mt-2
                border
                focus:border-blue-500 focus:bg-white focus:outline-none
              "
            ></textarea>
          </div>
          <div>
            <label class="block text-gray-700 text-left">Phone number</label>
            <input
              @blur="v$.body.phone_number.$touch"
              type="text"
              v-model="body.phone_number"
              placeholder="Enter Phone number"
              class="
                w-full
                px-4
                py-2
                rounded-lg
                bg-gray-200
                mt-2
                border
                focus:border-blue-500 focus:bg-white focus:outline-none
              "
            />
            <span
              v-if="v$.body.phone_number.$error"
              class="
                flex
                items-center
                font-medium
                tracking-wide
                text-red-500 text-xs
                mt-1
                ml-1
              "
            >
              {{ v$.body.phone_number.required.$message }},
            </span>
          </div>
          <div>
            <label class="block text-gray-700 text-left my-3"
              >Profile picture</label
            >
            <div class="mt-1 flex items-center">
              <input
                @change="imageChangeHandler"
                id="change-profile"
                type="file"
                class="hidden"
              />

              <span
                class="
                  inline-block
                  h-20
                  w-20
                  rounded-full
                  overflow-hidden
                  bg-gray-100
                "
              >
                <img
                  style=""
                  ref="image_display"
                  id="image-display"
                  class="object-cover w-full h-full"
                  :class="!has_image ? 'hidden' : ''"
                  v-bind:src="'' + image_display"
                  alt=""
                />

                <svg
                  class="h-full w-full text-gray-300"
                  :class="has_image ? 'hidden' : ''"
                  fill="currentColor"
                  viewBox="0 0 24 24"
                >
                  <path
                    d="M24 20.993V24H0v-2.996A14.977 14.977 0 0112.004 15c4.904 0 9.26 2.354 11.996 5.993zM16.002 8.999a4 4 0 11-8 0 4 4 0 018 0z"
                  />
                </svg>
              </span>
              <label
                for="change-profile"
                type="button"
                class="
                  ml-5
                  bg-white
                  py-2
                  px-3
                  border border-gray-300
                  rounded-md
                  shadow-sm
                  text-sm
                  leading-4
                  font-medium
                  text-gray-700
                  hover:bg-gray-50
                  focus:outline-none
                  focus:ring-2
                  focus:ring-offset-2
                  focus:ring-indigo-500
                "
              >
                Change
              </label>
            </div>
          </div>
        </div>
        <div class="flex justify-between">
          <a href=""></a>

          <button
            type="submit"
            class="
              inline-flex
              items-center
              px-4
              py-2
              font-semibold
              leading-6
              text-sm
              shadow
              rounded-md
              text-white
              bg-indigo-500
              hover:bg-indigo-400
              transition
              ease-in-out
              duration-150
            "
            :class="!is_loaded ? 'cursor-not-allowed' : ''"
          >
            <svg
              v-if="!is_loaded"
              class="animate-spin -ml-1 mr-3 h-5 w-5 text-white"
              xmlns="http://www.w3.org/2000/svg"
              fill="none"
              viewBox="0 0 24 24"
            >
              <circle
                class="opacity-25"
                cx="12"
                cy="12"
                r="10"
                stroke="currentColor"
                stroke-width="4"
              ></circle>
              <path
                class="opacity-75"
                fill="currentColor"
                d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"
              ></path>
            </svg>
            {{ is_loaded ? "Save" : "Saving...." }}
          </button>
        </div>
      </form>
    </div>
  </div>
</template>

<script>
import useVuelidate from "@vuelidate/core";
import { required, email, sameAs } from "@vuelidate/validators";
import { useStore } from "vuex";
import { PROFILE, UPDATE_USER } from "../../store/type";
import { computed } from "vue";

export default {
  props: ["showModal"],
  data() {
    const store = useStore();
    return {
      v$: useVuelidate(),
      error_raise: "",
      profile: computed(() => store.state.auth.profile),
      is_loaded: computed(() => store.state.auth.is_loaded),
      image_display: "",
      default_image: false,
      body: {
        first_name: "",
        last_name: "",
        phone_number: "",
        profile: "",
        date_of_birth: "",
        bio: "",
        address: "",
        school_work: "",
      },
      has_image: false,
      updateUserStore(profile) {
        if (
          profile.split(":")[0] == process.env.VUE_APP_STORAGE.split(":")[0]
        ) {
          profile = this.profile.profile;
        } else {
          profile = profile.split("base64,")[1];
        }
        store.dispatch({
          type: UPDATE_USER,
          body: {
            ...this.body,
            id: this.profile.id,
            profile: profile,
          },
        });
        store.dispatch(PROFILE);
      },
    };
  },

  computed: {
    image_url: function () {
      return document.getElementById("image-display");
    },
  },
  created() {
    this.$nextTick(() => {
      this.body = this.profile
      if (this.profile.profile) {
        this.has_image = true;
        this.image_url.setAttribute(
          "src",
          process.env.VUE_APP_STORAGE + this.profile.profile
        );
      }
    });
  },

  methods: {
    closeFunc() {
      console.log("welcome");
    },
    registerForm(e) {
      e.preventDefault();
    },
    test: function () {
      this.image_display = "";
    },
    imageChangeHandler: function (e) {
      this.$refs.value = "dina";

      var file = e.target.files[0];
      let doc = document.getElementById("image-display");

      var reader = new FileReader();
      reader.onloadend = function () {
        this.image_display = reader.result;
        let result = reader.result;
        doc.setAttribute("src", result);
        doc.classList.remove("hidden");
      };
      reader.readAsDataURL(file);
    },
    updateUser(e) {
      e.preventDefault();
      this.updateUserStore(this.image_url.getAttribute("src"));

      setTimeout(() => {
        this.$emit("close-modal");
        this.$swal.fire("Profile changed successfull", "", "success");
      }, 1000);
    },
  },

  watch: {},

  validations() {
    return {
      body: {
        first_name: { required },
        last_name: { required },
        phone_number: { required },
        email: { required, email },
        password: { required },
        date_of_birth: { required },
        profile: { required },
        confirm_password: {
          sameAsPassword: sameAs(this.body.password),
          required,
        },
      },
    };
  },
};
</script>

<style>
</style>