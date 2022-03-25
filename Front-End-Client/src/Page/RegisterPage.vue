<template>
  <section class="flex flex-col md:flex-row h-screen items-center">
    <div
      class="bg-indigo-600 hidden lg:block w-full md:w-1/2 xl:w-2/3 h-screen"
    >
      <img
        src="https://images.unsplash.com/photo-1492684223066-81342ee5ff30?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxzZWFyY2h8Mnx8ZXZlbnR8ZW58MHx8MHx8&w=1000&q=80"
        alt=""
        class="w-full h-full object-cover"
      />
    </div>

    <div
      class="
        bg-white
        w-full
        md:max-w-md
        lg:max-w-full
        md:mx-auto md:mx-0 md:w-1/2
        xl:w-1/3
        h-screen
        px-6
        lg:px-16
        xl:px-12
        flex
        items-center
        justify-center
      "
    >
      <div class="w-full h-100 relative">
        <h1 class="text-xl md:text-2xl font-bold leading-tight mt-12">
          Register
        </h1>
        <div class="flex absolute top-1 left-1 hover:underline cursor-pointer">
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
              d="M15 19l-7-7 7-7"
            /></svg
          >
           <router-link to="/"><a>Home</a></router-link>
        </div>

        <form @submit="registerForm" class="mt-6" action="#" method="POST">
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
            <label class="block text-gray-700 text-left">Last name</label>
            <select
              @blur="v$.body.gender.$touch"
              v-model="body.gender"
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
            >
              <option value="male">Male</option>
              <option value="female">Female</option>
            </select>
            <span
              v-if="v$.body.gender.$error"
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
              {{ v$.body.gender.required.$message }},
            </span>
          </div>
          <div>
            <label class="block text-gray-700 text-left">Email Address</label>
            <input
              @blur="v$.body.email.$touch"
              type="email"
              v-model="body.email"
              placeholder="Enter Email Address"
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
              autofocus
              autocomplete
              required
            />
            <span
              v-if="v$.body.email.$error || error_raise"
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
              {{ error_raise ? error_raise : "" }}
              {{ !error_raise ? v$.body.email.email.$message : "" }},
              {{ !error_raise ? v$.body.email.required.$message : "" }}
            </span>
          </div>
          <div class="mt-4">
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

          <div class="mt-4">
            <label class="block text-gray-700 text-left">Password</label>
            <input
              @blur="v$.body.password.$touch"
              type="password"
              v-model="body.password"
              placeholder="Enter Password"
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
          </div>
          <span
            v-if="v$.body.password.$error"
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
            {{ v$.body.password.required.$message }},
          </span>
          <div class="mt-4">
            <label class="block text-gray-700 text-left"
              >Confirm password</label
            >
            <input
              @blur="v$.body.confirm_password.$touch"
              type="password"
              v-model="body.confirm_password"
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
              v-if="v$.body.confirm_password.$error"
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
              {{
                v$.body.confirm_password.sameAsPassword.$invalid
                  ? "password confirmation doesn't match"
                  : ""
              }},
            </span>
          </div>

          <div class="text-right mt-2">
            <a
              href="#"
              class="
                text-sm
                font-semibold
                text-gray-700
                hover:text-blue-700
                focus:text-blue-700
              "
              >Forgot Password?</a
            >
          </div>

          <button
            type="submit"
            class="
              w-full
              block
              bg-indigo-500
              hover:bg-indigo-400
              focus:bg-indigo-400
              text-white
              font-semibold
              rounded-lg
              px-4
              py-2
              mt-6
            "
          >
            Register
          </button>
        </form>

        <hr class="my-6 border-gray-300 w-full" />

        <p class="mt-8">
          Have an account?
          <router-link to="/login">
            <a href="#" class="text-blue-500 hover:text-blue-700 font-semibold"
              >Login to existing account</a
            >
          </router-link>
        </p>
      </div>
    </div>
  </section>
</template>

<script>
import useVuelidate from "@vuelidate/core";
import { required, email, sameAs } from "@vuelidate/validators";
// import { computed } from 'vue'
import { useStore } from "vuex";
import { REGISTER } from "../store/type";
import { computed } from "vue-demi";

export default {
  name: "LoginPage",
  data() {
    const store = useStore();
    return {
      body: {
        first_name: "",
        last_name: "",
        phone_number: "",
        email: "",
        password: "",
        confirm_password: "",
        profile: "",
        date_of_birth: "",
        gender: ""
      },
      error_raise: computed(() => store.state.auth.error_raise),
      v$: useVuelidate(),
      register() {
        store.dispatch({ type: REGISTER, credential: this.body });
      },
    };
  },
  methods: {
    registerForm(e) {
      e.preventDefault();
      this.register();
    },
  },
  validations() {
    return {
      body: {
        first_name: { required },
        last_name: { required },
        phone_number: { required },
        email: { required, email },
        password: { required },
        date_of_birth: { required },
        gender: {required},
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