namespace phongcoursework
{
    partial class Form1
    {
        /// <summary>
        ///  Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        ///  Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        ///  Required method for Designer support - do not modify
        ///  the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            lblInput = new Label();
            txtInput = new TextBox();
            lblShift = new Label();
            txtShift = new TextBox();
            btnEncode = new Button();
            btnSort = new Button();
            lblOutput = new Label();
            txtOutput = new TextBox();
            lstAsciiCodes = new ListBox();
            SuspendLayout();
            // 
            // lblInput
            // 
            lblInput.AutoSize = true;
            lblInput.Location = new Point(32, 43);
            lblInput.Name = "lblInput";
            lblInput.Size = new Size(143, 15);
            lblInput.TabIndex = 0;
            lblInput.Text = "Input String(A-z,max 40):\"";
            // 
            // txtInput
            // 
            txtInput.Location = new Point(195, 43);
            txtInput.Name = "txtInput";
            txtInput.Size = new Size(100, 23);
            txtInput.TabIndex = 1;
            // 
            // lblShift
            // 
            lblShift.AutoSize = true;
            lblShift.Location = new Point(32, 87);
            lblShift.Name = "lblShift";
            lblShift.Size = new Size(108, 15);
            lblShift.TabIndex = 2;
            lblShift.Text = "Shift N (-25 to 25):\"";
            // 
            // txtShift
            // 
            txtShift.Location = new Point(195, 84);
            txtShift.Name = "txtShift";
            txtShift.Size = new Size(100, 23);
            txtShift.TabIndex = 3;
            // 
            // btnEncode
            // 
            btnEncode.Location = new Point(339, 52);
            btnEncode.Name = "btnEncode";
            btnEncode.Size = new Size(75, 23);
            btnEncode.TabIndex = 4;
            btnEncode.Text = "Encode";
            btnEncode.UseVisualStyleBackColor = true;
            btnEncode.Click += btnEncode_Click;
            // 
            // btnSort
            // 
            btnSort.Location = new Point(339, 107);
            btnSort.Name = "btnSort";
            btnSort.Size = new Size(75, 23);
            btnSort.TabIndex = 5;
            btnSort.Text = "Sort";
            btnSort.UseVisualStyleBackColor = true;
            btnSort.Click += btnSort_Click;
            // 
            // lblOutput
            // 
            lblOutput.AutoSize = true;
            lblOutput.Location = new Point(42, 170);
            lblOutput.Name = "lblOutput";
            lblOutput.Size = new Size(97, 15);
            lblOutput.TabIndex = 6;
            lblOutput.Text = "Encoded Output ";
            // 
            // txtOutput
            // 
            txtOutput.Location = new Point(168, 170);
            txtOutput.Name = "txtOutput";
            txtOutput.Size = new Size(246, 23);
            txtOutput.TabIndex = 7;
            txtOutput.Text = "Read Only";
            // 
            // lstAsciiCodes
            // 
            lstAsciiCodes.FormattingEnabled = true;
            lstAsciiCodes.ItemHeight = 15;
            lstAsciiCodes.Location = new Point(67, 242);
            lstAsciiCodes.Name = "lstAsciiCodes";
            lstAsciiCodes.Size = new Size(347, 124);
            lstAsciiCodes.TabIndex = 8;
            // 
            // Form1
            // 
            AutoScaleDimensions = new SizeF(7F, 15F);
            AutoScaleMode = AutoScaleMode.Font;
            ClientSize = new Size(800, 450);
            Controls.Add(lstAsciiCodes);
            Controls.Add(txtOutput);
            Controls.Add(lblOutput);
            Controls.Add(btnSort);
            Controls.Add(btnEncode);
            Controls.Add(txtShift);
            Controls.Add(lblShift);
            Controls.Add(txtInput);
            Controls.Add(lblInput);
            Name = "Form1";
            Text = "Form1";
            ResumeLayout(false);
            PerformLayout();
        }

        #endregion

        private Label lblInput;
        private TextBox txtInput;
        private Label lblShift;
        private TextBox txtShift;
        private Button btnEncode;
        private Button btnSort;
        private Label lblOutput;
        private TextBox txtOutput;
        private ListBox lstAsciiCodes;
    }
}
