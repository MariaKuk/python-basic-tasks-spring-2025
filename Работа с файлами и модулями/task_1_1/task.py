function fetchInternships() {
  var sheet = SpreadsheetApp.getActiveSpreadsheet().getActiveSheet();
  sheet.clearContents();
  sheet.appendRow(['Дата публикации', 'Название стажировки', 'Компания', 'Город', 'Формат', 'Срок подачи заявки', 'Ссылка на вакансию']);

  var url = 'https://career.habr.com/vacancies?type=internship&city_id=678'; // Москва
  var response = UrlFetchApp.fetch(url);
  var content = response.getContentText();
