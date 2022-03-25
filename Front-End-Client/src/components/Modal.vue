<template>
  <transition name="modal" id="modal-template">
    <div class="modal-mask">
      <div class="modal-wrapper">
        <div class="modal-container relative">
          <div class="modal-header">
            <button
              class="
                text-center
                absolute
                top-2
                right-2
                rounded-full
                mr-2
                modal-default-button
                ml-5
                bg-white
                py-2
                px-3
                border border-gray-300
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
                w-10
                h-10
              "
              ref=myBtn
              @click="$emit('close')"
            >
              <svg
                xmlns="http://www.w3.org/2000/svg"
                class="h-5 w-5 pr-1"
                fill="none"
                viewBox="0 0 24 24"
                stroke="currentColor"
              >
                <path
                  stroke-linecap="round"
                  stroke-linejoin="round"
                  stroke-width="2"
                  d="M6 18L18 6M6 6l12 12"
                />
              </svg>
            </button>
            <slot name="header"></slot>
          </div>

          <div class="modal-body">
            <slot name="body"></slot>
          </div>
          <div class="modal-footer">
            <slot name="footer"> </slot>
          </div>
        </div>
      </div>
    </div>
  </transition>
</template>

<script>
export default {

};
</script>

<style>
.modal-mask {
  position: fixed;
  z-index: 9998;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.5);
  display: table;
  transition: opacity 0.3s ease;
}

.modal-wrapper {
  display: table-cell;
  vertical-align: middle;
}

.modal-container {
  max-width: 1050px;
  margin: 0px auto;
  border-radius: 5px !important;
  box-shadow: 5px 5px #f000 !important;
  padding: 20px 30px;
  background-color: #fff;
  max-height: 90%;
  border-radius: 2px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.33);
  transition: all 0.3s ease;
  font-family: Helvetica, Arial, sans-serif;
  height: 821px;
  justify-content: center;
  display: flex;
  flex-direction: column;
  overflow: scroll;
}

.modal-header h3 {
  margin-top: 0;
  color: #42b983;
}

.modal-body {
  margin: 20px 0;
}

.modal-default-button {
  float: right;
}

/*
 * The following styles are auto-applied to elements with
 * transition="modal" when their visibility is toggled
 * by Vue.js.
 *
 * You can easily play with the modal transition by editing
 * these styles.
 */

.modal-enter {
  opacity: 0;
}

.modal-leave-active {
  opacity: 0;
}

.modal-enter .modal-container,
.modal-leave-active .modal-container {
  -webkit-transform: scale(1.1);
  transform: scale(1.1);
}
</style>