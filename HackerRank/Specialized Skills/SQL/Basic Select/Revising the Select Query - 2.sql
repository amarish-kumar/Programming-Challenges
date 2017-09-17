/**********************************************************************************************
** HackerRank Challenge - Revising the Select Query - 2                                      **
**      SQL / Basic Select                                                                   **
**                                                                                           **
** https://www.hackerrank.com/challenges/revising-the-select-query-2                         **
**                                                                                           **
** Query the names of all American cities in CITY with populations larger than 120,000. The  **
** CountryCode for America is USA.                                                           **
**                                                                                           **
** ====Input Format====                                                                      **
** The CITY table is described as follows:                                                   **
**                                                                                           **
**              CITY                                                                         **
** ================================                                                          **
** | Field        | Type          |                                                          **
** ================================                                                          **
** | ID           | NUMBER        |                                                          **
** --------------------------------                                                          **
** | NAME         | VARCHAR2 (17) |                                                          **
** --------------------------------                                                          **
** | COUNTRYCODE  | VARCHAR2 (3)  |                                                          **
** --------------------------------                                                          **
** | DISTRICT     | VARCHAR2 (20) |                                                          **
** --------------------------------                                                          **
** | Population   | NUMBER        |                                                          **
** --------------------------------                                                          **
**                                                                                           **
**********************************************************************************************/

Select name from city where countryCode = "USA" and population > 120000;