using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace phongcoursework
{
    using System;
    using System.Linq;

    public class StringProcessing
    {
        // Private fields
        private string s;
        private int n;

        // Public properties with validation
        public string S
        {
            get { return s; }
            set
            {
                if (value.Length <= 40 && value.All(c => char.IsUpper(c)))
                {
                    s = value;
                }
                else
                {
                    throw new ArgumentException("Input must be up to 40 capital letters only (A-Z).");
                }
            }
        }

        public int N
        {
            get { return n; }
            set
            {
                if (value >= -25 && value <= 25)
                {
                    n = value;
                }
                else
                {
                    throw new ArgumentException("Shift value must be between -25 and 25.");
                }
            }
        }

        // Constructor
        public StringProcessing(string input, int shift)
        {
            S = input;
            N = shift;
        }

        // Encode method
        public string Encode()
        {
            char[] output = new char[s.Length];

            for (int i = 0; i < s.Length; i++)
            {
                int offset = (s[i] - 'A' + n + 26) % 26;
                output[i] = (char)('A' + offset);
            }

            return new string(output);
        }

        // Print method
        public string Print()
        {
            return Encode();
        }

        // InputCode method
        public int[] InputCode()
        {
            return s.Select(c => (int)c).ToArray();
        }

        // OutputCode method
        public int[] OutputCode()
        {
            return Encode().Select(c => (int)c).ToArray();
        }

        // Sort method
        public string Sort()
        {
            char[] chars = s.ToCharArray();
            Array.Sort(chars);
            return new string(chars);
        }
    }
}

