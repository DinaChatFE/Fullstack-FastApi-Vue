<template>
  <section class="flex flex-col md:flex-row h-screen items-center">
    <div class="bg-indigo-600 hidden lg:block w-full md:w-1/2 xl:w-2/3 h-screen">
      <img
        src="https://images.unsplash.com/photo-1492684223066-81342ee5ff30?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxzZWFyY2h8Mnx8ZXZlbnR8ZW58MHx8MHx8&w=1000&q=80"
        alt="" class="w-full h-full object-cover" />
    </div>

    <div class="
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
      ">
      <div class="w-full h-100 relative">
        <h1 class="text-xl md:text-2xl font-bold leading-tight mt-12">
          Register
        </h1>
        <div @click="backLink" class="pr-3 py-1 rounded-md flex absolute top-1 left-1 hover:underline cursor-pointer">
          <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 19l-7-7 7-7" />
          </svg>
          <a>{{ step == 1 ? 'Home' : "Back" }}</a>
        </div>

        <form @submit="registerForm" class="mt-6" action="#" method="POST">
          <div class="step-1" v-show="step == 1">

            <div class="my-2">
              <label class="block text-gray-400 text-left">First name</label>
              <input v-model="body.first_name" @blur="v$.body.first_name.$touch" type="text"
                placeholder="Enter First name" class="
                w-full
                px-4
                py-2
                rounded-lg
                bg-gray-200
                mt-2
                border
                focus:border-blue-500 focus:bg-white focus:outline-none
              " />
              <span v-if="v$.body.first_name.$error" class="
                flex
                items-center
                font-medium
                tracking-wide
                text-red-500 text-xs
                mt-1
                ml-1
              ">
                {{ v$.body.first_name.required.$message }},
              </span>
            </div>
            <div class="my-2">
              <label class="block text-gray-400 text-left">Last name</label>
              <input @blur="v$.body.last_name.$touch" v-model="body.last_name" type="text" placeholder="Enter Last name"
                class="
                w-full
                px-4
                py-2
                rounded-lg
                bg-gray-200
                mt-2
                border
                focus:border-blue-500 focus:bg-white focus:outline-none
              " />
              <span v-if="v$.body.last_name.$error" class="
                flex
                items-center
                font-medium
                tracking-wide
                text-red-500 text-xs
                mt-1
                ml-1
              ">
                {{ v$.body.last_name.required.$message }},
              </span>
            </div>
            <div class="my-2">
              <label class="block text-gray-400 text-left">Date of birth</label>
              <input @blur="v$.body.date_of_birth.$touch" type="date" v-model="body.date_of_birth"
                placeholder="Enter Phone number" class="
                w-full
                px-4
                py-2
                rounded-lg
                bg-gray-200
                mt-2
                border
                focus:border-blue-500 focus:bg-white focus:outline-none
              " />
              <span v-if="v$.body.date_of_birth.$error" class="
                flex
                items-center
                font-medium
                tracking-wide
                text-red-500 text-xs
                mt-1
                ml-1
              ">
                {{ v$.body.date_of_birth.required.$message }},
              </span>
            </div>
            <div class="my-2">
              <label class="block text-gray-400 text-left">Phone number</label>
              <input @blur="v$.body.phone_number.$touch" type="text" v-model="body.phone_number"
                placeholder="Enter Phone number" class="
                w-full
                px-4
                py-2
                rounded-lg
                bg-gray-200
                mt-2
                border
                focus:border-blue-500 focus:bg-white focus:outline-none
              " />
              <span v-if="v$.body.phone_number.$error" class="
                flex
                items-center
                font-medium
                tracking-wide
                text-red-500 text-xs
                mt-1
                ml-1
              ">
                {{ v$.body.phone_number.required.$message }},
              </span>
            </div>
          </div>
          <div class="step-2" v-show="step == 2">
            <div class="my-2">
              <label class="block text-gray-400 text-left">Email Address</label>
              <input @blur="v$.stepBody.email.$touch" type="email" v-model="stepBody.email"
                placeholder="Enter Email Address" class="
                w-full
                px-4
                py-2
                rounded-lg
                bg-gray-200
                mt-2
                border
                focus:border-blue-500 focus:bg-white focus:outline-none
              " autofocus autocomplete required />
              <span v-if="v$.stepBody.email.$error || error_raise" class="
                flex
                items-center
                font-medium
                tracking-wide
                text-red-500 text-xs
                mt-1
                ml-1
              ">
                {{ error_raise ? error_raise : "" }}
                {{ !error_raise ? v$.stepBody.email.email.$message : "" }},
                {{ !error_raise ? v$.stepBody.email.required.$message : "" }}
              </span>
            </div>


            <div class="my-2">
              <label class="block text-gray-400 text-left">Password</label>
              <input @blur="v$.stepBody.password.$touch" type="password" v-model="stepBody.password"
                placeholder="Enter Password"
                class="w-full px-4 py-2 rounded-lg bg-gray-200 mt-2 border focus:border-blue-500 focus:bg-white focus:outline-none" />
              <span v-if="v$.stepBody.password.$error" class="flex items-center font-medium tracking-wide text-red-500 text-xs mt-1 ml-1
            ">
                {{ v$.body.stepBody.password.required.$message }},
              </span>
            </div>
            <div class="my-2">
              <label class="block text-gray-400 text-left">Confirm password</label>
              <input @blur="v$.stepBody.confirm_password.$touch" type="password" v-model="stepBody.confirm_password"
                placeholder="Enter Confirm password" minlength="6" class="w-full px-4 py-2 rounded-lg bg-gray-200 mt-2 border focus:border-blue-500 focus:bg-white focus:outline-none
              " />
              <span v-if="v$.stepBody.confirm_password.$error" class="flex items-center font-medium tracking-wide text-red-500 text-xs mt-1 ml-1
              ">
                {{
                  v$.stepBody.confirm_password.sameAsPassword.$invalid
                  ? "password confirmation doesn't match"
                  : ""
                }},
              </span>
            </div>

            <div class="text-right mt-2">
              <a href="#" class="text-sm font-semibold text-gray-400 hover:text-blue-700 focus:text-blue-700
              ">Forgot Password?</a>
            </div>
          </div>
          <button @click="submitAll" class=" w-full block bg-indigo-500 hover:bg-indigo-400 focus:bg-indigo-400 text-white font-semibold rounded-lg px-4 py-2 mt-6
            ">
            Register
          </button>
        </form>

        <hr class="my-6 border-gray-300 w-full" />
        <p class="mt-8">
          Have an account?
          <router-link to="/login">
            <a href="#" class="text-blue-500 hover:text-blue-700 font-semibold">Login to existing account</a>
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
import { useRoute } from 'vue-router';

export default {
  name: "LoginPage",
  methods: {
    backLink: function() {
      if (this.step === 1) {
        this.$router.push('/')
      } else {
        this.step = 1;
        this.$router.push('?step=1')
      }
    },  
    submitAll: async function (e) {
      e.preventDefault()
      if (this.step == 1) {
        if (await this.v$.body.$validate()) {
          this.$router.push('?step=2')
          this.step = 2;
        }
      }
      if (this.step == 2) {
        if (await this.v$.stepBody.$validate()) {
          console.log('validate');
          this.store.dispatch({ type: REGISTER, credential: { 
              ...this.body, 
              ...this.stepBody, 
              gender: '', 
              school_work: '',
              address: '',
              profile: ''
            }
          });
        }
      }
    },
    registerForm(e) {
      e.preventDefault();
      this.register();
    },
  },
  data() {
    const store = useStore();
    return {
      store,
      step: 1,
      body: {
        first_name: "",
        last_name: "",
        phone_number: "",
        date_of_birth: ""
      },
      stepBody: {
        email: "",
        password: "",
        confirm_password: "",
      },
      error_raise: computed(() => store.state.auth.error_raise),
      v$: useVuelidate(),
      register() {
        store.dispatch({ type: REGISTER, credential: this.body });
      },
    };
  },
  onMounted() {
    const route = useRoute();
    this.step = route.query.step ?? 1;
  },
  validations() {
    return {
      body: {
        first_name: { required },
        last_name: { required },
        phone_number: { required },
        date_of_birth: { required }
      },
      stepBody: {
        email: { required, email },
        password: { required },
        confirm_password: {
          sameAsPassword: sameAs(this.stepBody.password),
          required,
        },
      }
    };
  },
};
</script>