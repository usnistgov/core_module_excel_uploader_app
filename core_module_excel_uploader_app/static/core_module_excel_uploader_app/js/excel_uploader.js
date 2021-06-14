saveExcelUploaderData = function() {
    return new FormData($($("#modal-" + moduleElement[0].id)[0]).find(".excel-uploader-form")[0]);
}

let excelUploaderPopupOptions = {
    title: "Upload Excel File",
    getData: saveExcelUploaderData
}

configurePopUp('module-excel-uploader', excelUploaderPopupOptions);