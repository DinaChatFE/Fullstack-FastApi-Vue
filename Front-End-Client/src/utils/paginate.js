
export default {
    getLinkCount: (dataList)=> {        
        return Math.floor(dataList/process.env.VUE_APP_COUNT_PAGE) + 1
    }
}