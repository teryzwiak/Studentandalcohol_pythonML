he model aimed to assess the impact of daily habits (including alcohol consumption) on the chances of passing the final exam.

The initial dataset we adopted contained irrelevant data, which we removed:

Place of residence (city, suburb/village)
Family size (smaller or equal to 3; larger than 3)
Parental relationship status (living together or separated)
Parents' education (divided into columns per parent)
Parents' occupation (same as above)
Reason for choosing the school (good location, prestige, quality of education, or others)
Legal guardian of the student (mother or father)
School attended (GP or MS, abbreviation of the name)
Family relationships
Our goal was to estimate only the final exam (column G3), but the correlation matrix showed that the results at the end of the first and second semesters (G1 and G2, respectively) strongly influence the final exam outcome. Based on the test we conducted by removing these columns, the model made significant errors in predicting students' grades.

During model training, we found that the best-performing model was the Random Forest Regressor, which achieved an accuracy measured by the MAE method at the level of 79.83%. Manual tests indicated that this accuracy level is sufficient - for a diligent student who obtained nearly perfect scores in all exams (19, 19, and 20, respectively), the regressor predicted a score of 19 points, while the student actually received 20.

Improving the model by increasing the default number of built trees (from 100 to 200) during training resulted in a 0.1 percentage point improvement. This was the maximum value we were able to achieve.
