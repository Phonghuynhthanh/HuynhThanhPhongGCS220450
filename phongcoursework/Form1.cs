namespace phongcoursework
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void btnEncode_Click(object sender, EventArgs e)
        {
            try
            {
                string input = txtInput.Text;
                int shift = int.Parse(txtShift.Text);

                StringProcessing processor = new StringProcessing(input, shift);

                string encoded = processor.Encode();
                txtOutput.Text = encoded;

                lstAsciiCodes.Items.Clear();

                string inputCodes = string.Join(", ", processor.InputCode());
                string outputCodes = string.Join(", ", processor.OutputCode());

                lstAsciiCodes.Items.Add("Input ASCII Codes: " + inputCodes);
                lstAsciiCodes.Items.Add("Output ASCII Codes: " + outputCodes);
            }
            catch (Exception ex)
            {
                MessageBox.Show("Error: " + ex.Message);
            }
        }

        private void btnSort_Click(object sender, EventArgs e)
        {
            try
            {
                string input = txtInput.Text;
                int shift = int.Parse(txtShift.Text);

                StringProcessing processor = new StringProcessing(input, shift);

                string sorted = processor.Sort();
                MessageBox.Show("Sorted String: " + sorted);
            }
            catch (Exception ex)
            {
                MessageBox.Show("Error: " + ex.Message);
            }
        }
    } // close class Form1
}     // ✅ close namespace phongcoursework
